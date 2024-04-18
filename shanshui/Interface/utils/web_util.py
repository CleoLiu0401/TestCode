from Interface.utils.log_util import logger


def click_exception(by,element,max_attempts=5):
    def _inner(driver):
        #多次点击按钮
        actul_attempts = 0
        while actul_attempts < max_attempts:
            actul_attempts += 1
            try:
                driver.find_element(by,element).click()
                return True
            except Exception:
                logger.debug("点击出现异常")
        #当实际点击次数大于最大点击次数，结束循环
        raise Exception("超出最大点击次数")
    return _inner()