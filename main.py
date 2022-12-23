from expect import Interactor
from app import ServerControl
def main():
    app = ServerControl()
    app.start_server()
    app.run()

main()