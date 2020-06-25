import cv2
import numpy as np
import os

#待处理图片目录
font_dir="CNfont"
#图像文件输出目录
output="processed"
#待处理字体清单
folders=os.listdir(font_dir)
#attrgan 字体文件夹名称
gan=["Acme-Regular","Actor-Regular","Adamina-Regular"]

if __name__ == "__main__":
    #遍历待处理清单
    for f_index,folder in enumerate(folders):
        img_list=os.listdir(font_dir+'/'+folder)
        #每个清单内只提取前三张图片
        for index,gan_name in enumerate(gan):
            #图像名称
            img_name=font_dir+'/'+folder+'/'+img_list[index]
            #读取图片为灰度图像
            img=cv2.imread(img_name,cv2.IMREAD_GRAYSCALE)
            #将图像调整为256*256
            img=cv2.resize(img,(256,256))
            #图像10位
            ten=int(f_index/10)
            #图像个位
            units=int(f_index%10)
            #输出文件名称
            output_name=output+"/"+gan_name+"/"+str(ten)+str(units)+".png"
            #输出文件
            cv2.imwrite(output_name,img)
        print("生成进度：",f_index+1,"/",len(folders))
    print("---------图像处理完成--------")
