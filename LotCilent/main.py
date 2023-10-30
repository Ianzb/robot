from widgets import *


class MainPage(ScrollArea):
    """
    主页
    """
    name = "LotCilent"

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(self.name)
        self.toolBar = ToolBar(self.name, "LotCilent", self)
        self.setViewportMargins(0, self.toolBar.height(), 0, 0)

        self.view = QWidget(self)
        self.setWidget(self.view)
        self.view.setStyleSheet("QWidget {background-color: rgba(0,0,0,0); border: none}")

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, self.toolBar.height(), 0, 0)
        self.setWidgetResizable(True)

        self.vBoxLayout = QVBoxLayout(self.view)
        self.vBoxLayout.setSpacing(30)
        self.vBoxLayout.setAlignment(Qt.AlignTop)
        self.vBoxLayout.setContentsMargins(36, 20, 36, 36)

        self.lineEdit = SearchLineEdit(self)
        self.lineEdit.searchButton.setEnabled(False)
        self.lineEdit.searchButton.hide()
        self.pushButton = PrimaryPushButton("搜索", self, FIF.SEARCH)
        self.grayCard1 = GrayCard("搜索", self.view)
        self.grayCard1.addWidget(self.lineEdit)
        self.grayCard1.addWidget(self.pushButton, Qt.AlignRight)

        self.card1 = PhotoCard("D:\编程\program\Windows\img\logo.png", "zb小程序", self)
        self.card1.connect(lambda: print("123"))

        self.grayCard2 = GrayCard("信息", self.view)
        self.grayCard2.addWidget(self.card1)

        self.vBoxLayout.addWidget(self.grayCard1)
        self.vBoxLayout.addWidget(self.grayCard2)


class Window(FluentWindow):
    """
    主窗口
    """

    def __init__(self):
        super().__init__()
        self.setObjectName("主窗口")

        self.__initWindow()
        self.__initWidget()

    def __initWindow(self):
        """
        窗口初始化
        """
        # 外观调整
        setTheme(Theme.AUTO)
        setThemeColor("#0078D4")
        # 窗口属性
        self.resize(900, 700)
        self.setWindowIcon(QIcon(program.source("logo.png")))
        self.setWindowTitle(program.PROGRAM_NAME)
        self.navigationInterface.setReturnButtonVisible(False)
        # 窗口居中
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def __initWidget(self):
        """
        组件初始化
        """

        self.mainPage = MainPage(self)
        self.addSubInterface(self.mainPage, FIF.HOME, self.mainPage.name, NavigationItemPosition.TOP)
        self.navigationInterface.addSeparator(NavigationItemPosition.TOP)

    def keyPressEvent(self, QKeyEvent):
        """
        自定义按键事件
        """
        # Esc键
        if QKeyEvent.key() == Qt.Key_Escape:
            self.hide()


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    translator = FluentTranslator()
    app.installTranslator(translator)
    w = Window()
    w.show()
    app.exec_()
