import json
from mcp.server.fastmcp import FastMCP
from seedance_2_5_spicy_api import Seedance25SpicyAPI

# Initialize FastMCP server
mcp = FastMCP("Seedance 2.5 Spicy API Server")


def get_api():
    return Seedance25SpicyAPI()


@mcp.tool()
def text_to_video(prompt: str, aspect_ratio: str = "16:9", duration: int = 5, resolution: str = "720p",
                   generate_audio: bool = True, camera_fixed: bool = False, high_bitrate: bool = False,
                   draft: bool = False, draft_request_id: str = None) -> str:
    """
    Generate photorealistic 4K video from a text prompt using Seedance 2.5 Spicy (relaxed content moderation).

    :param resolution: '480p', '720p', '1080p', or '4k'. Price scales with resolution.
    :param draft: Generate a cheap 480p draft to finalize later with draft_request_id.
    """
    api = get_api()
    result = api.text_to_video(prompt, aspect_ratio, duration, resolution, generate_audio, camera_fixed, high_bitrate, draft, draft_request_id)
    return json.dumps(result, indent=2)


@mcp.tool()
def image_to_video(prompt: str, image_url: str, last_image: str = None, duration: int = 5, resolution: str = "720p",
                    generate_audio: bool = True, camera_fixed: bool = False, high_bitrate: bool = False,
                    draft: bool = False, draft_request_id: str = None) -> str:
    """
    Animate a single image into photorealistic 4K video using Seedance 2.5 Spicy.
    """
    api = get_api()
    result = api.image_to_video(prompt, image_url, last_image, duration, resolution, generate_audio, camera_fixed, high_bitrate, draft, draft_request_id)
    return json.dumps(result, indent=2)


@mcp.tool()
def first_last_frame(prompt: str, images_list: list[str], resolution: str = "720p", duration: int = 5,
                      seed: int = -1, high_bitrate: bool = False, draft: bool = False, draft_request_id: str = None) -> str:
    """
    Generate a smooth video transition between a start and end image using Seedance 2.5 Spicy.

    :param images_list: Exactly 2 images: [first_frame, last_frame].
    """
    api = get_api()
    result = api.first_last_frame(prompt, images_list, resolution, duration, seed, high_bitrate, draft, draft_request_id)
    return json.dumps(result, indent=2)


@mcp.tool()
def omni_reference(prompt: str, images_list: list[str] = None, videos_list: list[str] = None,
                    audios_list: list[str] = None, resolution: str = "720p", duration: int = 5,
                    aspect_ratio: str = "16:9", omni_reference_task_type: str = "auto", seed: int = -1,
                    high_bitrate: bool = False, draft: bool = False, draft_request_id: str = None) -> str:
    """
    Blend up to 30 reference images, 10 video clips, and 10 audio files into a single guided generation using Seedance 2.5 Spicy Omni Reference.
    """
    api = get_api()
    result = api.omni_reference(prompt, images_list, videos_list, audios_list, resolution, duration, aspect_ratio, omni_reference_task_type, seed, high_bitrate, draft, draft_request_id)
    return json.dumps(result, indent=2)


@mcp.tool()
def video_edit(prompt: str, video_url: str, images_list: list[str] = None, audios_list: list[str] = None,
               resolution: str = "720p", duration: int = 5, generate_audio: bool = True, seed: int = -1,
               high_bitrate: bool = False) -> str:
    """
    Edit an input video from a natural-language prompt using Seedance 2.5 Spicy Video Edit.
    """
    api = get_api()
    result = api.video_edit(prompt, video_url, images_list, audios_list, resolution, duration, generate_audio, seed, high_bitrate)
    return json.dumps(result, indent=2)


@mcp.tool()
def video_extend(prompt: str, video_url: str, last_image: str = None, resolution: str = "720p", duration: int = 5,
                  generate_audio: bool = True, seed: int = -1, high_bitrate: bool = False) -> str:
    """
    Extend an input video with a new cinematic continuation using Seedance 2.5 Spicy Video Extend.
    """
    api = get_api()
    result = api.video_extend(prompt, video_url, last_image, resolution, duration, generate_audio, seed, high_bitrate)
    return json.dumps(result, indent=2)


@mcp.tool()
def motion_control(video_url: str, images_list: list[str] = None, prompt: str = None, aspect_ratio: str = "16:9",
                    duration: int = 5, seed: int = -1, high_bitrate: bool = False, generate_audio: bool = False) -> str:
    """
    Recast an existing performance video with a bolder creative treatment while preserving motion, choreography, and camera work — Seedance 2.5 Spicy Motion Control.
    """
    api = get_api()
    result = api.motion_control(video_url, images_list, prompt, aspect_ratio, duration, seed, high_bitrate, generate_audio)
    return json.dumps(result, indent=2)


@mcp.tool()
def upload_file(file_path: str) -> str:
    """
    Upload a local file (image, video, or audio) to MuAPI for use in generation tasks.
    """
    api = get_api()
    result = api.upload_file(file_path)
    return json.dumps(result, indent=2)


@mcp.tool()
def get_task_status(request_id: str) -> str:
    """
    Check the status and get results of a generation task.
    """
    api = get_api()
    result = api.get_result(request_id)
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    mcp.run()
