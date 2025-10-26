from ui.main import Ui_MainWindow

def v_proxy(input_widget, parent=None):
    proxy_text = input_widget.toPlainText().strip()
    if proxy_text.startswith(("http://", "https://")) or proxy_text == "":
        return proxy_text if proxy_text else None
    else:
        Ui_MainWindow.show_custom_warning(parent, "Error", "Proxy must start with http:// or https://")
        input_widget.clear()
        return None



def v_delay(input_widget, parent=None):
    delay_text = input_widget.toPlainText().strip()
    try:
        delays = [int(x) for x in delay_text.split()]
    except ValueError:
        Ui_MainWindow.show_custom_warning(parent, "Error", "Invalid delay (Must be number)")
        input_widget.clear()
        return None

    if any(delay <= 0 for delay in delays):
        Ui_MainWindow.show_custom_warning(parent, "Error", "Delay cannot be ≤ 0")
        input_widget.clear()
        return None

    return delays
