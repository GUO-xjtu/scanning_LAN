from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
import sys


class ToolsUi(QDialog):
    # 信号槽机制：设置一个信号，用于触发接收区写入动作
    signal_write_msg_logo = QtCore.pyqtSignal(str)
    signal_write_msg_message = QtCore.pyqtSignal(str)

    def __init__(self, num):
        """
        初始化窗口
        :param num: 计数窗口
        """
        super(ToolsUi, self).__init__()
        self.num = num
        self._translate = QtCore.QCoreApplication.translate

        self.setObjectName("局域网设备扫描")
        self.resize(640, 480)
        self.setAcceptDrops(False)
        self.setSizeGripEnabled(False)

        # 定义控件
        self.pushButton_get_ip = QtWidgets.QPushButton()
        self.pushButton_link = QtWidgets.QPushButton()
        self.pushButton_unlink = QtWidgets.QPushButton()
        self.pushButton_clear = QtWidgets.QPushButton()
        self.pushButton_exit = QtWidgets.QPushButton()
        self.pushButton_send = QtWidgets.QPushButton()
        # self.pushButton_dir = QtWidgets.QPushButton()
        self.pushButton_else = QtWidgets.QPushButton()
        self.label_port = QtWidgets.QLabel()
        self.label_ip = QtWidgets.QLabel()
        self.label_rev_logo = QtWidgets.QLabel()
        self.label_rev_message = QtWidgets.QLabel()
        self.label_sendto = QtWidgets.QLabel()
        # self.label_dir = QtWidgets.QLabel()
        self.label_written = QtWidgets.QLabel()
        self.lineEdit_port = QtWidgets.QLineEdit()
        self.lineEdit_ip_send = QtWidgets.QLineEdit()
        self.lineEdit_ip_local = QtWidgets.QLineEdit()
        self.textBrowser_recv_message = QtWidgets.QTextBrowser()
        self.textBrowser_recv_logo = QtWidgets.QTextBrowser()
        self.comboBox_message = QtWidgets.QComboBox()

        # 定义布局
        self.h_box_1 = QHBoxLayout()
        self.h_box_2 = QHBoxLayout()
        self.h_box_3 = QHBoxLayout()
        self.h_box_4 = QHBoxLayout()
        self.h_box_recv = QHBoxLayout()
        self.h_box_exit = QHBoxLayout()
        self.h_box_all = QHBoxLayout()
        self.v_box_set = QVBoxLayout()
        self.v_box_recv = QVBoxLayout()
        self.v_box_web = QVBoxLayout()
        self.v_box_exit = QVBoxLayout()
        self.v_box_right = QVBoxLayout()
        self.v_box_left = QVBoxLayout()

        self.lbl = QLabel(self)
        # 向选择功能的下拉菜单添加选项
        self.comboBox_message.addItem("")
        self.comboBox_message.addItem("")
        self.comboBox_message.addItem("")
        self.comboBox_message.addItem("")
        self.comboBox_message.addItem("")

        # 设置字体
        font = QtGui.QFont()
        font.setFamily("Yuppy TC")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_rev_logo.setFont(font)
        self.label_rev_message.setFont(font)

        # 设置控件的初始属性
        # self.label_dir.hide()
        self.label_sendto.hide()
        # self.pushButton_dir.hide()
        self.lineEdit_ip_send.hide()
        # self.label_dir.setWordWrap(True)  # 让label自动换行
        self.pushButton_unlink.setEnabled(False)
        self.textBrowser_recv_logo.insertPlainText("logo窗口-%s\n" % self.num)
        self.textBrowser_recv_message.insertPlainText("message窗口-%s\n" % self.num)
        # 调用布局方法和控件显示文字的方法
        self.layout_ui()
        self.ui_translate()
        self.connect()

    def layout_ui(self):
        """
        设置控件的布局
        :return:
        """
        # 左侧布局添加
        self.h_box_1.addWidget(self.label_ip)
        self.h_box_1.addWidget(self.lineEdit_ip_local)
        self.h_box_1.addWidget(self.pushButton_get_ip)
        self.h_box_2.addWidget(self.label_port)
        self.h_box_2.addWidget(self.lineEdit_port)
        self.h_box_2.addWidget(self.pushButton_else)
        self.h_box_3.addWidget(self.label_sendto)
        self.h_box_3.addWidget(self.lineEdit_ip_send)
        self.h_box_4.addWidget(self.comboBox_message)
        self.h_box_4.addWidget(self.pushButton_link)
        self.h_box_4.addWidget(self.pushButton_unlink)
        self.v_box_set.addLayout(self.h_box_1)
        self.v_box_set.addLayout(self.h_box_2)
        self.v_box_set.addLayout(self.h_box_3)
        self.v_box_set.addLayout(self.h_box_4)
        # self.v_box_web.addWidget(self.label_dir)
        # self.v_box_web.addWidget(self.pushButton_dir)
        # self.v_box_send.addWidget(self.label_send)
        self.v_box_recv.addWidget(self.label_rev_message)
        self.v_box_left.addLayout(self.v_box_recv)
        self.v_box_recv.addWidget(self.textBrowser_recv_message)
        # self.v_box_exit.addWidget(self.pushButton_send)
        self.v_box_exit.addWidget(self.pushButton_exit)
        self.h_box_exit.addWidget(self.label_written)
        self.h_box_exit.addLayout(self.v_box_exit)
        self.v_box_left.addLayout(self.v_box_set)
        self.v_box_left.addLayout(self.v_box_recv)
        self.v_box_left.addLayout(self.h_box_exit)

        # 右侧布局添加
        self.h_box_recv.addWidget(self.label_rev_logo)
        self.h_box_recv.addWidget(self.pushButton_clear)
        self.v_box_right.addLayout(self.h_box_recv)
        self.v_box_right.addWidget(self.lbl)

        # 将左右布局添加到窗体布局
        self.h_box_all.addLayout(self.v_box_left)
        self.h_box_all.addLayout(self.v_box_right)

        # 设置窗体布局到窗体
        self.setLayout(self.h_box_all)

    def ui_translate(self):
        """
        控件默认显示文字的设置
        :param : QDialog类创建的对象
        :return: None
        """
        # 设置各个控件显示的文字
        # 也可使用控件的setText()方法设置文字
        self.setWindowTitle(self._translate("diandian", "局域网设备扫描工具-窗口%s" % self.num))
        self.comboBox_message.setItemText(0, self._translate("diandian", "PU设备"))
        self.comboBox_message.setItemText(1, self._translate("diandian", "网桥"))
        self.comboBox_message.setItemText(2, self._translate("diandian", "摄像头"))
        self.comboBox_message.setItemText(3, self._translate("diandian", "硬件板"))
        self.comboBox_message.setItemText(4, self._translate("diandian", "投影仪"))
        self.pushButton_link.setText(self._translate("diandian", "生成logo"))
        self.pushButton_unlink.setText(self._translate("diandian", "开始扫描"))
        self.pushButton_get_ip.setText(self._translate("diandian", "重新获取IP"))
        self.pushButton_clear.setText(self._translate("diandian", "清除消息"))
        self.pushButton_send.setText(self._translate("diandian", "打印"))
        self.pushButton_exit.setText(self._translate("diandian", "退出系统"))

        self.pushButton_else.setText(self._translate("diandian", "窗口多开another"))
        self.label_ip.setText(self._translate("diandian", "本机IP:"))
        self.label_port.setText(self._translate("diandian", "端口号:"))

        self.label_rev_logo.setText(self._translate("diandian", "logo展示区域"))
        self.label_rev_message.setText(self._translate("diandian", "信息生成区域"))

        self.label_written.setText(self._translate("diandian", "Written by 点点智联"))

    def connect(self):
        """
        控件信号-槽的设置
        :param : QDialog类创建的对象
        :return: None
        """
        self.signal_write_msg_logo.connect(self.write_msg_logo)
        self.signal_write_msg_message.connect(self.write_msg_messge)
        # self.comboBox_tcp.currentIndexChanged.connect(self.combobox_change)

    # def combobox_change(self):
    #     # 此函数用于选择不同功能时界面会作出相应变化
    #     """
    #     combobox控件内容改变时触发的槽
    #     :return: None
    #     """
    #     self.close_all()
    #     if self.comboBox_tcp.currentIndex() == 0 or self.comboBox_tcp.currentIndex() == 2:
    #         self.label_sendto.hide()
    #         self.label_dir.hide()
    #         self.pushButton_dir.hide()
    #         self.pushButton_send.show()
    #         self.lineEdit_ip_send.hide()
    #         self.textEdit_send.show()
    #         self.label_port.setText(self._translate("TCP-UDP", "端口号:"))
    #
    #     if self.comboBox_tcp.currentIndex() == 1 or self.comboBox_tcp.currentIndex() == 3:
    #         self.label_sendto.show()
    #         self.label_dir.hide()
    #         self.pushButton_dir.hide()
    #         self.pushButton_send.show()
    #         self.lineEdit_ip_send.show()
    #         self.textEdit_send.show()
    #         self.label_port.setText(self._translate("TCP-UDP", "目标端口:"))
    #
    #     if self.comboBox_tcp.currentIndex() == 4:
    #         self.label_sendto.hide()
    #         self.label_dir.show()
    #         self.pushButton_dir.show()
    #         self.pushButton_send.hide()
    #         self.lineEdit_ip_send.hide()
    #         self.textEdit_send.hide()
    #         self.label_port.setText(self._translate("TCP-UDP", "端口号:"))

    def write_msg_logo(self, msg):
        # signal_write_msg信号会触发这个函数
        """
        功能函数，向接收区写入数据的方法
        信号-槽触发
        tip：PyQt程序的子线程中，直接向主线程的界面传输字符是不符合安全原则的
        :return: None
        """
        pixmap = QPixmap(r"C:\Users\Administrator\PycharmProjects\untitled\project\print_device\diandian.png")
        self.textBrowser_recv_logo.insertPlainText(msg)
        self.lbl.setPixmap(pixmap)
        self.lbl.setScaledContents(True)
        self.setLayout(self.v_box_right)

        # 滚动条移动到结尾
        self.textBrowser_recv_logo.moveCursor(QtGui.QTextCursor.End)

    def write_msg_messge(self, msg):
        # signal_write_msg信号会触发这个函数
        """
        功能函数，向接收区写入数据的方法
        信号-槽触发
        tip：PyQt程序的子线程中，直接向主线程的界面传输字符是不符合安全原则的
        :return: None
        """
        self.textBrowser_recv_message.insertPlainText(msg)
        # 滚动条移动到结尾
        self.textBrowser_recv_message.moveCursor(QtGui.QTextCursor.End)

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        self.close_all()

    def close_all(self):
        pass


if __name__ == '__main__':
    """
    显示界面
    """
    app = QApplication(sys.argv)
    ui = ToolsUi(1)
    ui.show()
    sys.exit(app.exec_())
