from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import *


class PhotoCard(ElevatedCardWidget):
    """
    大图片卡片
    """

    def __init__(self, icon: str, name: str = "名称", parent=None):
        super().__init__(parent)
        self.iconWidget = ImageLabel(icon, self)
        self.label = CaptionLabel(name, self)
        self.label.setStyleSheet("QLabel {background-color: rgba(0,0,0,0); border: none;}")

        self.iconWidget.scaledToHeight(68)

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setAlignment(Qt.AlignCenter)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.iconWidget, 0, Qt.AlignCenter)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.label, 0, Qt.AlignHCenter | Qt.AlignBottom)

        self.setFixedSize(168, 176)

    def mousePressEvent(self, event):
        self.clickedFunction()

    def connect(self, functions):
        self.clickedFunction = functions

    def clickedFunction(self):
        pass


class GrayCard(QWidget):
    """
    灰色背景组件卡片
    """

    def __init__(self, title: str, parent=None, alignment=Qt.AlignLeft):
        super().__init__(parent=parent)

        self.titleLabel = StrongBodyLabel(title, self)
        self.card = QFrame(self)
        self.card.setObjectName("卡片")

        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout(self.card)

        self.vBoxLayout.setSizeConstraint(QVBoxLayout.SetMinimumSize)
        self.hBoxLayout.setSizeConstraint(QHBoxLayout.SetMinimumSize)

        self.vBoxLayout.setSpacing(12)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)

        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignTop)
        self.vBoxLayout.addWidget(self.card, 0, Qt.AlignTop)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(12, 12, 12, 12)
        self.hBoxLayout.setAlignment(alignment)

        self.setTheme()
        qconfig.themeChanged.connect(self.setTheme)

    def addWidget(self, widget: object, spacing=0, alignment=Qt.AlignTop):
        self.hBoxLayout.addWidget(widget, alignment=alignment)
        self.hBoxLayout.addSpacing(spacing)

    def setTheme(self):
        if isDarkTheme():
            self.setStyleSheet("QLabel {background-color: transparent; color: white}")
            self.card.setStyleSheet("QWidget {background-color: rgba(25,25,25,0.5); border:1px solid rgba(20,20,20,0.15); border-radius: 10px}")
        else:
            self.setStyleSheet("QLabel {background-color: transparent; color: black}")
            self.card.setStyleSheet("QWidget {background-color: rgba(175,175,175,0.1); border:1px solid rgba(150,150,150,0.15); border-radius: 10px}")


class ScrollArea(ScrollArea):
    """
    优化样式的滚动区域
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("QScrollArea {background-color: rgba(0,0,0,0); border: none; border-top-left-radius: 10px;}")


class ToolBar(QWidget):
    """
    页面顶端工具栏
    """

    def __init__(self, title, subtitle, parent=None):
        super().__init__(parent=parent)
        self.setFixedHeight(90)

        self.titleLabel = TitleLabel(title, self)
        self.subtitleLabel = CaptionLabel(subtitle, self)

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(36, 22, 36, 12)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addSpacing(4)
        self.vBoxLayout.addWidget(self.subtitleLabel)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

        self.setTheme()
        qconfig.themeChanged.connect(self.setTheme)

    def setTheme(self):
        if isDarkTheme():
            self.setStyleSheet("QLabel {background-color: transparent; color: white}")
        else:
            self.setStyleSheet("QLabel {background-color: transparent; color: black}")


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
        # self.setWindowIcon(QIcon(program.source("logo.png")))
        self.setWindowTitle("LotInterface")
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
