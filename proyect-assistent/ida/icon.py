from PyQt5.QtWidgets import QApplication, QSystemTrayIcon,QMenu
from PyQt5.QtGui import QIcon
import sys

def icono():
    app=QApplication(sys.argv)
    TrayIcon= QSystemTrayIcon(QIcon('D:\\Documentos\\Github\\Proyecto SOFTWARE\\rougue-studios\\resources\\iconoTask1000.png'),parent=app)
    TrayIcon.setToolTip('IDA')
    TrayIcon.show()

    menu=QMenu()
    exitAction=menu.addAction('Salir')
    exitAction.triggered.connect(app.quit)
    TrayIcon.setContextMenu(menu)

    sys.exit(app.exec_())


