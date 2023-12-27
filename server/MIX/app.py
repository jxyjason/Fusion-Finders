from flask import Flask, jsonify, request
import test

from PIL import Image

import sys
sys.path.append(r"LAVT-RIS-main")
import demo_inference

app = Flask(__name__)


# 这里默认的是get请求方式
@app.route('/hello', methods=["GET", "POST"])
def hello_world():
#这里面就是你想要返回给前端的值， 切记，这里只能返回字符串，如果是个json数据，你的通过json.dumps(你的json数据)
#  data = request.get_json()
#  videoName = data.get("videoName")
#  sentence = data.get("sentence")
 return '[10,201]'

    
@app.route('/locate', methods=["GET", "POST"])
def locate():
    data = request.get_json()
    vName = data.get("videoName")
    vSen = data.get("sentence")
    return test.beginLocation(vName,vSen)

@app.route('/detect', methods=["GET", "POST"])
def detect():
    data = request.get_json()
    rgb_str = data.get("rgb")
    vWidth = data.get("width")
    vHeight = data.get("height")
    vSen = data.get("sentence")

    # 解析RGB字符串，生成像素数据
    pixels = []
    count=0
    for rgb in rgb_str.split("_"):
        r, g, b = map(int, rgb.split(","))
        pixels.extend([(r, g, b)])
    # 创建一个空白的PIL.Image.Image对象
    img = Image.new("RGB", (vWidth, vHeight))
    # 将像素数据填充到PIL.Image.Image对象中
    img.putdata(pixels)

    return demo_inference.beginDetection(img,vWidth,vHeight,vSen)



if __name__ == '__main__':
    # 这里host是你的后端地址，这里写0.0.0.0， 表示的是这个接口在任何服务器上都可以被访问的到，只需要前端访问该服务器地址就可以的，
    # 当然你也可以写死，如222.222.222.222， 那么前端只能访问222.222.222.222, port是该接口的端口号,
    # debug = True ,表示的是，调试模式，每次修改代码后不用重新启动服务
    test.preProcessTAN()
    demo_inference.pre_lavt()
    app.run(host='0.0.0.0', port=9090)