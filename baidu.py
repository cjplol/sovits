from inference_main import main  #引用语音推理方法
import os

# 1.导入库  pip install baidu-aip
from aip import AipSpeech

if __name__=="__main__":
    # 2.初始化AipSpeech对象
    App_ID = '31464582'
    API_Key = 'uNi0i8CDyLKpqgtQx1pBA6Pi'
    Secret_Key = '3WNDDfPyx2ChrYmUnmPL6zRa4gyK2m8y'
    
    # 相当于3把钥匙
    client = AipSpeech(App_ID, API_Key, Secret_Key)
    
    # 3.调用语音合成的方法
    str = '大家好，我是人工智能静芬，可以给你们唱歌哦'
    # 音频文件流
    result = client.synthesis(str, "zh", 1, {"per": 0})  #per：度小宇=1，度小美=0，度逍遥（基础）=3，度丫丫=4，精品音库：度逍遥（精品）=5003，度小鹿=5118，度博文=106，度小童=110，度小萌=111，度米朵=103，度小娇=5
    # print(result)
    
    # 识别正确返回语音二进制 错误则返回dict 参照错误码
    #4.保存音频文件
    if not isinstance(result, dict):
        with open('./raw/audio.mp3', 'wb') as f:
            f.write(result)

    #5 将百度音频转换为静芬语音
    os.system('python inference_main.py -m "logs/44k/G_24000.pth" -c "configs/config.json" -n "audio.mp3" -t 2 -s "jingfen"')