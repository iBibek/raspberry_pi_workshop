# Cloudflare Tunnel Setup for Raspberry Pi

## Install Cloudflared

**For 64-bit Pi (Pi 4/5):**

```bash
curl -L --output cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64.deb
sudo dpkg -i cloudflared.deb
```

**For 32-bit Pi (older models):**

```bash
curl -L --output cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-armhf.deb
sudo dpkg -i cloudflared.deb
```

## Run the Tunnel

Make sure your Flask server is running first, then:

```bash
cloudflared tunnel --url http://localhost:5000
```

This will output a public URL like `https://something-random.trycloudflare.com` that you can access from anywhere.

No account or signup required.
