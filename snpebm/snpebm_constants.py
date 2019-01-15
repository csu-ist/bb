SNPE_SDK_ROOT = 'SNPE_ROOT'
# for running as a SNPE contributor
ZDL_ROOT = 'ZDL_ROOT'
SNPE_BENCH_NAME = 'snpe_bench'
SNPE_BENCH_ROOT = 'SNPE_BENCH_ROOT'
SNPE_BENCH_LOG_FORMAT = '%(asctime)s - %(levelname)s - {}: %(message)s'

SNPE_BATCHRUN_EXE = 'snpe-net-run'
SNPE_RUNTIME_LIB = 'libSNPE.so'
SNPE_BATCHRUN_GPU_S_EXE = 'snpe-net-run-g'
SNPE_RUNTIME_GPU_S_LIB = 'libSNPE_G.so'

SNPE_BENCH_SCRIPT = 'snpe-bench_cmds.sh'
SNPE_DLC_INFO_EXE = "snpe-dlc-info"
SNPE_DIAGVIEW_EXE = "snpe-diagview"
DEVICE_TYPE_ARM_ANDROID = 'arm_android'
DEVICE_TYPE_ARM_LINUX = 'arm_linux'
DEVICE_ID_X86 = 'localhost'
ARTIFACT_DIR = "artifacts"
SNPE_BENCH_DIAG_OUTPUT_FILE = "SNPEDiag_0.log"
SNPE_BENCH_DIAG_REMOVE = "SNPEDiag*"
SNPE_BENCH_OUTPUT_DIR_DATETIME_FMT = "%4d-%02d-%02d_%02d:%02d:%02d"
SNPE_BENCH_ANDROID_ARM32_ARTIFACTS_JSON = "snpebm_artifacts.json"
SNPE_BENCH_ANDROID_ARM32_LLVM_ARTIFACTS_JSON = "snpebm_artifacts_android_arm32_llvm.json"
SNPE_BENCH_ANDROID_AARCH64_ARTIFACTS_JSON = "snpebm_artifacts_android_aarch64.json"
SNPE_BENCH_ANDROID_AARCH64_LLVM_ARTIFACTS_JSON = "snpebm_artifacts_android_aarch64_llvm.json"
SNPE_BENCH_LE_ARTIFACTS_JSON = "snpebm_artifacts_le.json"
SNPE_BENCH_LE_GCC48_HF_ARTIFACTS_JSON = "snpebm_artifacts_le_gcc48hf.json"
SNPE_BENCH_LE64_GCC49_ARTIFACTS_JSON = "snpebm_artifacts_le64_gcc49.json"
SNPE_BENCH_LE64_GCC53_ARTIFACTS_JSON = "snpebm_artifacts_le64_gcc53.json"

CONFIG_DEVICEOSTYPES_ANDROID_ARM32 = 'android'
CONFIG_DEVICEOSTYPES_ANDROID_ARM32_LLVM = 'android-arm32-llvm'
CONFIG_DEVICEOSTYPES_ANDROID_AARCH64 = 'android-aarch64'
CONFIG_DEVICEOSTYPES_ANDROID_AARCH64_LLVM = 'android-aarch64-llvm'
CONFIG_DEVICEOSTYPES_LE = 'le'
CONFIG_DEVICEOSTYPES_LE_GCC48_HF = 'le_gcc4.8hf'
CONFIG_DEVICEOSTYPES_LE64_GCC49 = 'le64_gcc4.9'
CONFIG_DEVICEOSTYPES_LE64_GCC53 = 'le64_gcc5.3'

#some values in the JSON fields. used in JSON and in directory creation.
RUNTIME_CPU = "CPU"
RUNTIME_CPU_MODE_FXP8 = "CPU_FXP8"
RUNTIME_DSP = "DSP"
RUNTIME_GPU = "GPU"
RUNTIME_GPU_MODE_FP16 = "GPU_FP16"
RUNTIME_GPU_MODE_FP32 = "GPU_FP32"
GPU_MODE_FP16 = "float16"
GPU_MODE_DEFAULT = "default"
RUNTIME_GPU_ONLY = "GPU_s" #This is using GPU standalone libSNPE_G.so, which is built with -Os to optimize for space

ARCH_AARCH64 = "aarch64"
ARCH_ARM = "arm"
ARCH_DSP = "dsp"
ARCH_X86 = "x86"

PLATFORM_OS_LINUX = "linux"
PLATFORM_OS_ANDROID = "android"

COMPILER_GCC53 = "gcc5.3"
COMPILER_GCC49 = "gcc4.9"
COMPILER_GCC48 = "gcc4.8"
COMPILER_CLANG38 = "clang3.8"
STL_GNUSTL_SHARED = "gnustl_shared.so"
STL_LIBCXX_SHARED = "libc++_shared.so"

MEASURE_SNPE_VERSION = 'snpe_version'
MEASURE_TIMING = "timing"
MEASURE_MEM = "mem"
MEASURE_POWER = "power"
MEASURE_ACCURACY = "accuracy"

LATEST_RESULTS_LINK_NAME = "latest_results"

MEM_LOG_FILE_NAME = "MemLog.txt"
POWER_LOG_FILE_NAME = "power_output.json"
POWER_LOG_PLOT_NAME = "power_plot.png"

ERRNUM_CONFIG_ERROR = 1
ERRNUM_POWERMONITOR_ERROR = 2
ERRNUM_PARSEARGS_ERROR = 3
ERRNUM_GENERALEXCEPTION_ERROR = 4
ERRNUM_ADBSHELLCMDEXCEPTION_ERROR = 5
ERRNUM_MD5CHECKSUM_FILE_NOT_FOUND_ON_DEVICE = 14
ERRNUM_MD5CHECKSUM_CHECKSUM_MISMATCH = 15
ERRNUM_MD5CHECKSUM_UNKNOWN_ERROR = 16
ERRNUM_NOBENCHMARKRAN_ERROR = 17
