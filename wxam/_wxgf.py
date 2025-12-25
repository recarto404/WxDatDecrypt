import subprocess

def wxam_to_image(input_bytes: bytes, format) -> bytes:
    cmd = [
        'ffmpeg',
        '-hide_banner',
        '-loglevel', 'error',
        '-i', 'pipe:0',         # 输入自 stdin
        "-frames:v", "1",
        '-c:v', 'mjpeg',        # 视频编码器
        '-f', 'mjpeg',          # 输出格式
        'pipe:1'                # 输出到 stdout
    ]
    try:
        proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out, err = proc.communicate(input=input_bytes)
        if proc.returncode != 0:
            raise RuntimeError(f'ffmpeg error: {err.decode("utf-8")}')
        return out
    except Exception as e:
        raise RuntimeError(f"Failed to run ffmpeg: {e}")
