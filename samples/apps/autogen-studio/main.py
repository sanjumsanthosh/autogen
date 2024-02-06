import uvicorn
import os

if __name__ == "__main__":


    host: str = "127.0.0.1"
    port: int = 8082
    workers: int = 1
    reload = True
    docs: bool = False
    appdir: str = None

    os.environ["AUTOGENSTUDIO_API_DOCS"] = str(docs)
    if appdir:
        os.environ["AUTOGENSTUDIO_APPDIR"] = appdir


    uvicorn.run(
        "autogenstudio.web.app:app",
        host=host,
        port=port,
        workers=workers,
        reload=reload,
    )