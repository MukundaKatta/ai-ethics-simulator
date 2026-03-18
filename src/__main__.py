"""CLI for ai-ethics-simulator."""
import sys, json, argparse
from .core import AiEthicsSimulator

def main():
    parser = argparse.ArgumentParser(description="Simulate ethical dilemmas for AI systems and evaluate decision-making")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = AiEthicsSimulator()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.analyze(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"ai-ethics-simulator v0.1.0 — Simulate ethical dilemmas for AI systems and evaluate decision-making")

if __name__ == "__main__":
    main()
