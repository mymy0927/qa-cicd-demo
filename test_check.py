import urllib.request
import time

def test_baidu_status():
    print("开始执行自动化巡检任务...")
    url = "https://www.baidu.com"
    
    start_time = time.time()
    response = urllib.request.urlopen(url)
    status_code = response.getcode()
    end_time = time.time()
    
    print(f"访问 {url} 状态码: {status_code}")
    print(f"耗时: {round((end_time - start_time)*1000, 2)} ms")
    
    # 这里就是我们的“质量门禁”断言：如果不是200，直接报错
    assert status_code == 404, f"巡检失败！预期状态码 200，实际为 {status_code}"
    print("✅ 巡检通过，页面正常。")

if __name__ == "__main__":
    test_baidu_status()
