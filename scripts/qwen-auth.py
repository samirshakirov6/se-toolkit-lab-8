#!/usr/bin/env python3
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

def check_qwen_cli():
    if shutil.which("qwen"):
        print("✓ Qwen CLI is installed")
        return True
    print("✗ Qwen CLI is not installed")
    print("Install: pnpm add -g @qwen-code/qwen-code")
    return False

def run_qwen_login():
    print("\nRunning 'qwen login'...")
    try:
        result = subprocess.run(["qwen", "login"], capture_output=False, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        print("✗ 'qwen login' not found")
        return False
    except KeyboardInterrupt:
        print("\nInterrupted")
        return False

def verify_credentials():
    creds_path = Path.home() / ".qwen" / "oauth_creds.json"
    if not creds_path.exists():
        print(f"\n✗ Not found: {creds_path}")
        return False
    try:
        creds = json.loads(creds_path.read_text())
        print(f"\n✓ Found: {creds_path}")
        if not creds.get("access_token"):
            print("✗ No access_token")
            return False
        print("✓ Access token present")
        if not creds.get("refresh_token"):
            print("✗ No refresh_token")
            return False
        print("✓ Refresh token present")
        expiry_ms = creds.get("expiry_date", 0)
        if expiry_ms > time.time() * 1000:
            expiry_date = datetime.fromtimestamp(expiry_ms / 1000)
            print(f"✓ Token valid (expires: {expiry_date})")
        else:
            print(f"✗ Token expired")
            return False
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def main():
    print("=" * 50)
    print("Qwen OAuth Token Update")
    print("=" * 50)
    if not check_qwen_cli():
        return 1
    if not run_qwen_login():
        print("\n✗ Login failed")
        return 1
    if not verify_credentials():
        print("\n✗ Verification failed")
        return 1
    print("\n" + "=" * 50)
    print("✓ Token updated!")
    print("=" * 50)
    print("\nRestart proxy:")
    print("  docker compose --env-file .env.docker.secret restart qwen-code-api")
    return 0

if __name__ == "__main__":
    sys.exit(main())
