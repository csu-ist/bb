#!/system/bin/sh
export LD_LIBRARY_PATH=/data/local/tmp/snpebm/artifacts/arm-android-gcc4.9/lib:$LD_LIBRARY_PATH
export ADSP_LIBRARY_PATH="/data/local/tmp/snpebm/artifacts/arm-android-gcc4.9/lib/../../dsp/lib;/system/lib/rfsa/adsp;/usr/lib/rfsa/adsp;/system/vendor/lib/rfsa/adsp;/dsp"
cd /data/local/tmp/snpebm/SRN
rm -rf output
/data/local/tmp/snpebm/artifacts/arm-android-gcc4.9/bin/snpe-net-run --container srn_model_3L_16-32_0104_1.dlc --input_list raw_list_2.txt --output_dir output --use_gpu --userbuffer_float --perf_profile high_performance
