import re
import subprocess as sp


def get_resolution(input_path: str, ffprobe_path: str) -> tuple[int, int]:
    """
    image/video resolution.

    `input_path`: absolute path to the input file
    `ffprobe_path`: absolute path to ffprobe executable

    return: `(width, height)`
    """
    cmd = [
        ffprobe_path,
        '-v', 'error',
        '-select_streams', 'v',
        '-of', 'csv=p=0',
        '-show_entries', 'stream=width,height',
        input_path
    ]
    res = sp.run(cmd, capture_output=True, text=True)
    match = re.search(r'^(\d+),(\d+)$', res.stdout.strip())
    width, height = int(match.group(1)), int(match.group(2))
    return width, height


def get_audio_sample_rate(input_path: str, ffprobe_path: str) -> float:
    res = sp.check_output(
        [
            ffprobe_path, '-v', 'error',
            '-select_streams', 'a',
            '-of', 'csv=p=0',
            '-show_entries', 'stream=sample_rate',
            input_path
        ],
        stderr=sp.STDOUT, text=True
    )
    reg = re.match(r'^(?P<v>\d+(?:\.\d+)?)', res)
    return float(reg.group('v'))


def get_vid_dur(file: str, ffprobe: str, /) -> float:
    """
    Get video duration in secs.
    Note, video and audio might be different.
    `file`: full path to the input file
    `ffprobe`: ffprobe.exe full path
    """
    stdout = sp.check_output(
        [
            ffprobe, '-v', 'error',
            '-select_streams', 'v',
            '-of', 'csv=p=0',
            '-show_entries', 'stream=duration',
            file
        ],
        stderr=sp.STDOUT, text=True
    )
    res = re.match(r'^(?P<dur>\d+(?:\.\d+)?)', stdout)
    return float(res.group('dur'))

def get_audio_dur(file: str, ffprobe: str, /) -> float:
    """
    Get audio duration in secs.
    Note, video and audio might be different.
    `file`: full path to the input file
    `ffprobe`: ffprobe.exe full path
    """
    stdout = sp.check_output(
        [
            ffprobe, '-v', 'error',
            '-select_streams', 'a',
            '-of', 'csv=p=0',
            '-show_entries', 'stream=duration',
            file
        ],
        stderr=sp.STDOUT, text=True
    )
    res = re.match(r'^(?P<dur>\d+(?:\.\d+)?)', stdout)
    return float(res.group('dur'))


def get_vid_fps(file: str, ffprobe: str, /, *, do_round: bool = False) -> int | float:
    """
    Video fps (average frame rate).

    `file`: full path to the input file
    `ffprobe`: ffprobe.exe full path
    `do_round`: round the fps to the nearest integer
    """
    stdout = sp.check_output(
        [
            ffprobe, '-v', 'error',
            '-select_streams', 'v',
            '-of', 'csv=p=0',
            '-show_entries', 'stream=avg_frame_rate',
            file
        ],
        stderr=sp.STDOUT, text=True
    )
    res = re.match(r'^(?P<fps>\d+/\d+)', stdout)
    fps = eval(res.group('fps'), {})
    if do_round:
        return round(fps)
    else:
        return fps