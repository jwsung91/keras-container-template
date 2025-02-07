import platform
import tensorflow as tf
import keras

def check_cuda():
    print("TensorFlow Version:", tf.__version__)
    print("CUDA Available:", tf.config.list_physical_devices('GPU'))

    try:
        tf.debugging.set_log_device_placement(True)
        gpu_devices = tf.config.list_physical_devices('GPU')
        if gpu_devices:
            print("Available GPU:", gpu_devices)
        else:
            print("No GPU detected.")
    except Exception as e:
        print("Error:", e)

def check_tf_keras():
    print("🔥 Checking TensorFlow & Keras versions...\n")
    print(f"🖥️ OS: {platform.system()} {platform.release()} ({platform.architecture()[0]})")

    print(f"🐍 Python Version: {platform.python_version()}")

    try:
        print(f"\n🟢 TensorFlow Version: {tf.__version__}")
        print(f"📦 Keras Version: {keras.__version__}")

        gpu_devices = tf.config.list_physical_devices('GPU')
        print(f"🔧 CUDA Available (TensorFlow): {len(gpu_devices) > 0}")

        if gpu_devices:
            print(f"🖥️ GPU Devices: {[device.name for device in gpu_devices]}")
    except Exception as e:
        print(f"⚠️ TensorFlow Error: {e}")

if __name__ == "__main__":
    check_cuda()
    check_tf_keras()
