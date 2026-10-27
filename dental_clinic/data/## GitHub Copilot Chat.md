## GitHub Copilot Chat

- Extension: 0.65.0 (prod)
- VS Code: 1.137.0 (645f29cc3176500b4b5762ba887cf2a7f0ffdf2c)
- OS: linux 7.0.0-31-generic x64
- GitHub Account: abdomahmod876-bot

## Network

User Settings:
```json
  "http.systemCertificatesNode": true,
  "telemetry.telemetryLevel": "all",
  "github.copilot.advanced.debug.useElectronFetcher": true,
  "github.copilot.advanced.debug.useNodeFetcher": false,
  "github.copilot.advanced.debug.useNodeFetchFetcher": true
```

Connecting to https://api.github.com:
- DNS ipv4 Lookup: 20.199.39.228 (1 ms)
- DNS ipv6 Lookup: Error (65 ms): getaddrinfo ENOTFOUND api.github.com
- Proxy URL: None (57 ms)
- Electron fetch (configured): HTTP 200 (88 ms)
- Node.js https: HTTP 200 (523 ms)
- Node.js fetch: HTTP 200 (555 ms)

Connecting to https://api.individual.githubcopilot.com/_ping:
- DNS ipv4 Lookup: 140.82.114.22 (2 ms)
- DNS ipv6 Lookup: Error (4 ms): getaddrinfo ENOTFOUND api.individual.githubcopilot.com
- Proxy URL: None (57 ms)
- Electron fetch (configured): HTTP 200 (164 ms)
- Node.js https: HTTP 200 (500 ms)
- Node.js fetch: HTTP 200 (579 ms)

Connecting to https://proxy.individual.githubcopilot.com/_ping:
- DNS ipv4 Lookup: 20.199.39.224 (0 ms)
- DNS ipv6 Lookup: Error (53 ms): getaddrinfo ENOTFOUND proxy.individual.githubcopilot.com
- Proxy URL: None (10 ms)
- Electron fetch (configured): HTTP 200 (64 ms)
- Node.js https: HTTP 200 (273 ms)
- Node.js fetch: HTTP 200 (252 ms)

Connecting to https://mobile.events.data.microsoft.com/OneCollector/1.0?cors=true&content-type=application/x-json-stream (Electron fetch): HTTP 200 (76 ms)
Connecting to https://telemetry.individual.githubcopilot.com/telemetry (Node.js https): HTTP 200 (452 ms)
Connecting to https://default.exp-tas.com/vscode/ab (Node.js fetch): HTTP 200 (406 ms)

Number of system certificates: 365

## Notes

- Active fetcher: Electron fetch.
- For corporate networks also see: [Troubleshooting firewall settings for GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot).