import argparse
import os
import uvicorn


def extract_args() -> dict:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--host", type=str, help="Host for the server to run on", default="127.0.0.1")
    arg_parser.add_argument("--port", type=int, help="Port for the server to run on", default=9090)
    args = arg_parser.parse_args()
    return {'host': args.host, 'port': args.port}


def main(host: str | None, port: int | None) -> None:
    print(f"Start server...")
    uvicorn.run(
        app="src.server:app",
        host=host if host else '127.0.0.1',
        port=port if port else 9090,
        reload=True
    )


if __name__ == '__main__':
    args = extract_args()
    main(host=args['host'], port=args['port'])