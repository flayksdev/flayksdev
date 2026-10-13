#!/usr/bin/env python3
"""Gera assets/stats.svg com números públicos do perfil, sem serviços de terceiros.

Usa apenas a biblioteca padrão. Variáveis de ambiente:
  GITHUB_TOKEN        token do GitHub Actions (leitura de dados públicos)
  USERNAME            usuário do GitHub (padrão: flayksdev)
  STATS_PLACEHOLDER   se "1", gera um cartão inicial sem consultar a API
"""
import datetime
import html
import json
import os
import urllib.request

USERNAME = os.environ.get("USERNAME", "flayksdev")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "stats.svg")

F = "Inter, 'SF Pro Display', 'Segoe UI', Helvetica, Arial, sans-serif"
CY, CY2, CY3 = "#22D3EE", "#67E8F9", "#A5F3FC"
TXT, MUT = "#F0F7FF", "#9DB6DC"


def api(path, data=None):
    url = "https://api.github.com" + path
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-stats"}
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collect():
    user = api(f"/users/{USERNAME}")
    repos = api(f"/users/{USERNAME}/repos?per_page=100&type=owner")
    own = [r for r in repos if not r.get("fork")]
    stars = sum(r.get("stargazers_count", 0) for r in own)
    langs = {}
    for r in own:
        try:
            for lang, size in api(f"/repos/{USERNAME}/{r['name']}/languages").items():
                langs[lang] = langs.get(lang, 0) + size
        except Exception:
            pass
    contributions = None
    try:
        q = {
            "query": "query($u:String!){user(login:$u){contributionsCollection{contributionCalendar{totalContributions}}}}",
            "variables": {"u": USERNAME},
        }
        res = api("/graphql", q)
        contributions = res["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    except Exception:
        pass
    return {
        "repos": user.get("public_repos", len(own)),
        "stars": stars,
        "followers": user.get("followers", 0),
        "contributions": contributions,
        "langs": langs,
    }


def esc(s):
    return html.escape(str(s), quote=False)


def render(d, note):
    w, h = 1000, 300
    metrics = [
        ("REPOSITÓRIOS PÚBLICOS", d["repos"]),
        ("ESTRELAS RECEBIDAS", d["stars"]),
        ("SEGUIDORES", d["followers"]),
        ("CONTRIBUIÇÕES · 12 MESES", d["contributions"]),
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t">',
        f'<title id="t">Estatísticas públicas do GitHub de {esc(USERNAME)}</title>',
        f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#050A18"/><stop offset="1" stop-color="#0A1636"/></linearGradient>
<linearGradient id="bd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CY}" stop-opacity="0.8"/><stop offset="0.5" stop-color="#1E3A8A" stop-opacity="0.4"/><stop offset="1" stop-color="#2563EB" stop-opacity="0.7"/></linearGradient>
<linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2563EB"/><stop offset="1" stop-color="{CY}"/></linearGradient>
<pattern id="gr" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#5B8CFF" stroke-opacity="0.06"/></pattern>
</defs>''',
        f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" fill="url(#bg)"/>',
        f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" fill="url(#gr)"/>',
        f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" fill="none" stroke="url(#bd)" stroke-width="1.5"/>',
        f'<line x1="520" y1="34" x2="520" y2="244" stroke="#5B8CFF" stroke-opacity="0.2"/>',
    ]
    for i, (label, val) in enumerate(metrics):
        col, row = i % 2, i // 2
        x = 44 + col * 240
        y = 60 + row * 100
        shown = "—" if val is None else f"{val:,}".replace(",", ".")
        parts.append(f'<text x="{x}" y="{y}" font-family="{F}" font-size="12" font-weight="700" fill="{CY}" letter-spacing="2">{esc(label)}</text>')
        parts.append(f'<text x="{x}" y="{y+46}" font-family="{F}" font-size="44" font-weight="800" fill="{TXT}">{esc(shown)}</text>')

    parts.append(f'<text x="560" y="60" font-family="{F}" font-size="12" font-weight="700" fill="{CY}" letter-spacing="2">LINGUAGENS MAIS USADAS</text>')
    langs = sorted(d["langs"].items(), key=lambda kv: -kv[1])[:5]
    total = sum(v for _, v in d["langs"].items())
    if langs and total:
        for i, (name, size) in enumerate(langs):
            y = 92 + i * 34
            pct = size / total * 100
            parts.append(f'<text x="560" y="{y+12}" font-family="{F}" font-size="15" font-weight="600" fill="#E0F7FF">{esc(name)}</text>')
            parts.append(f'<rect x="700" y="{y}" width="200" height="12" rx="6" fill="#5B8CFF" fill-opacity="0.15"/>')
            parts.append(f'<rect x="700" y="{y}" width="{max(6, 200*pct/100):.0f}" height="12" rx="6" fill="url(#bar)"/>')
            parts.append(f'<text x="916" y="{y+11}" font-family="{F}" font-size="14" fill="{MUT}">{pct:.0f}%</text>')
    else:
        parts.append(f'<text x="560" y="110" font-family="{F}" font-size="15" fill="{MUT}">Os dados aparecem aqui assim que a primeira</text>')
        parts.append(f'<text x="560" y="134" font-family="{F}" font-size="15" fill="{MUT}">atualização automática for concluída.</text>')

    parts.append(f'<text x="44" y="{h-28}" font-family="{F}" font-size="12" fill="{MUT}">{esc(note)}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    if os.environ.get("STATS_PLACEHOLDER") == "1":
        data = {"repos": None, "stars": None, "followers": None, "contributions": None, "langs": {}}
        note = "Atualização automática diária · dados públicos da API do GitHub"
    else:
        data = collect()
        today = datetime.datetime.now(datetime.timezone.utc).strftime("%d/%m/%Y")
        note = f"Atualizado em {today} (UTC) · dados públicos da API do GitHub, sem contribuições privadas"
    svg = render(data, note)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print("stats.svg escrito")


if __name__ == "__main__":
    main()
