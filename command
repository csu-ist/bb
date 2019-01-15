
#########  dpc command ######### 
cd '/opt/SNPE/snpe-1.19.2/models/dpc' 

python '/opt/SNPE/snpe-1.19.2/models/dpc/scripts/setup_dpc.py'  -a '/opt/SNPE/snpe-1.19.2/models/dpc/tensorflow' 

cd $SNPE_ROOT/examples/NativeCpp/SampleCode

/opt/SNPE/snpe-1.19.2/examples/NativeCpp/SampleCode/obj/local/x86_64-linux-clang/snpe-sample -d '/opt/SNPE/snpe-1.19.2/models/dpc/dlc/0.01mask2_1.dlc'   -i '/opt/SNPE/snpe-1.19.2/models/dpc/data/cropped/raw_list.txt'   -o output1130-v0-dpc-256x256

python '/opt/SNPE/snpe-1.19.2/models/dpc/scripts/compose_dpc_raws.py' 

__get_img_raw("/opt/SNPE/snpe-1.19.2/models/dpc/data/cropped/3.jpg", "/opt/SNPE/snpe-1.19.2/examples/NativeCpp/SampleCode/output1130-v0-dpc-256x256/Result_1/conv_7/BiasAdd:0.raw")


######### sfr command  ######### 
cd '/opt/SNPE/snpe-1.19.2/models/srn' 

python '/opt/SNPE/snpe-1.19.2/models/srn/scripts/setup_srn.py'  -a '/opt/SNPE/snpe-1.19.2/models/srn/tensorflow' 

cd '/opt/SNPE/snpe-1.19.2/examples/NativeCpp/SampleCode'
make -f Makefile.x86_64-linux-clang 

/opt/SNPE/snpe-1.19.2/examples/NativeCpp/SampleCode/obj/local/x86_64-linux-clang/snpe-sample -d '/opt/SNPE/snpe-1.19.2/models/srn/dlc/srn_model_288_complex.dlc'    -i '/opt/SNPE/snpe-1.19.2/models/srn/data/target_raw_list_1.txt'   -o output1221-v0-srn-input_288x288

python '/opt/SNPE/snpe-1.19.2/models/srn/scripts/compose_srn_raws.py'


#########  environment setting: ######### 
进入root
export SNPE_ROOT=opt/SNPE/snpe-1.19.2/
export TENSORFLOW_HOME=/usr/local/lib/python2.7/dist-packages/tensorflow/
export ANDROID_NDK_ROOT=/home/sunny/下载/android-ndk-r11/
cd $SNPE_ROOT
source bin/envsetup.sh -t $TENSORFLOW_DIR
如果snpe版本没变更的话，环境配置就是这样，如果更新版本，则要修改SNPE_ROOT地址，若还是不行，则要参考/snpe-x.xx.x/doc/html/setup.html文档重新配置（需要连网，可能会涉及到python库的下载）


benchmarking command

# 连接好手机
adb root 
adb remount
adb devices   # 获取设备编号，若与srn_sample.json中的"Devices":["a28cdb00"]不一致，则修改
adb shell  # 进入手机的命令端
#查看手机里是否有/data/local/tmp/snpebm/SRN/raw/这个路径，没有则需要创建。查看： ls -R /data/local/
#创建： mkdir -p /data/local/tmp/snpebm/SRN/raw/
exit  #退出手机命令端
adb push /home/sunny/raw/handicap_sign.raw /data/local/tmp/snpebm/SRN/raw/  #将测试所需图片拷贝到手机中，尺寸大小为256x256,需跟模型输入尺寸匹配

cd $SNPE_ROOT/benchmarks
python snpe_bench.py -c srn_sample.json -a






