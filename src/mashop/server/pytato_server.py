from mashop.microtoolkit import MicroRestServer

server = MicroRestServer()
app = server.setup_app()

if __name__ == '__main__':
    server.start(app)
