import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Seedance25SpicyAPI:
    def __init__(self, api_key=None):
        """
        Initialize the Seedance 2.5 Spicy API client.
        :param api_key: Your MuAPI.ai API key. Defaults to MUAPI_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("MUAPI_API_KEY")
        if not self.api_key:
            raise ValueError("API Key is required. Set MUAPI_API_KEY in .env or pass it to the constructor.")

        self.base_url = "https://api.muapi.ai/api/v1"
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def text_to_video(self, prompt, aspect_ratio="16:9", duration=5, resolution="720p",
                       generate_audio=True, camera_fixed=False, high_bitrate=False,
                       draft=False, draft_request_id=None):
        """
        Submits a Seedance 2.5 Spicy Text-to-Video task. The relaxed-moderation variant
        of the Seedance 2.5 flagship model — photorealistic 4K video directly from a
        text prompt, with reduced content-safety filtering and more dramatic,
        higher-contrast motion than the standard tier.

        :param prompt: Text prompt describing the video scene and motion. Spicy mode
                       favors bolder, higher-contrast, more expressive results.
        :param aspect_ratio: 'adaptive', '16:9', '9:16', '1:1', '3:4', '4:3', or '21:9'.
        :param duration: Video duration in seconds (4-16).
        :param resolution: '480p', '720p', '1080p', or '4k'. Price scales with resolution.
        :param generate_audio: Whether to generate audio for the video.
        :param camera_fixed: Whether to fix the camera position.
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :param draft: Generate a cheap 480p draft (resolution must be 480p or omitted).
        :param draft_request_id: Finalize an earlier draft into a full 1080p render.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2.5-spicy-text-to-video"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "resolution": resolution,
            "generate_audio": generate_audio,
            "camera_fixed": camera_fixed,
            "high_bitrate": high_bitrate,
            "draft": draft,
        }
        if draft_request_id:
            payload["draft_request_id"] = draft_request_id
        return self._post_request(endpoint, payload)

    def image_to_video(self, prompt, image_url, last_image=None, duration=5, resolution="720p",
                        generate_audio=True, camera_fixed=False, high_bitrate=False,
                        draft=False, draft_request_id=None):
        """
        Submits a Seedance 2.5 Spicy Image-to-Video task. Animates a single image into
        photorealistic 4K video with reduced content-safety filtering and more dramatic,
        higher-contrast motion than the standard tier — with native audio generation
        and precise camera trajectory control.

        :param prompt: Text prompt describing the video motion and style.
        :param image_url: URL of the input image to animate into video.
        :param last_image: Optional URL of the last frame image for first-last frame control.
        :param duration: Video duration in seconds (4-16).
        :param resolution: '480p', '720p', '1080p', or '4k'. Price scales with resolution.
        :param generate_audio: Whether to generate audio for the video.
        :param camera_fixed: Whether to fix the camera position.
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :param draft: Generate a cheap 480p draft (resolution must be 480p or omitted).
        :param draft_request_id: Finalize an earlier draft into a full 1080p render.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2.5-spicy-image-to-video"
        payload = {
            "prompt": prompt,
            "image_url": image_url,
            "duration": duration,
            "resolution": resolution,
            "generate_audio": generate_audio,
            "camera_fixed": camera_fixed,
            "high_bitrate": high_bitrate,
            "draft": draft,
        }
        if last_image:
            payload["last_image"] = last_image
        if draft_request_id:
            payload["draft_request_id"] = draft_request_id
        return self._post_request(endpoint, payload)

    def first_last_frame(self, prompt, images_list, resolution="720p", duration=5, seed=-1,
                          high_bitrate=False, draft=False, draft_request_id=None):
        """
        Submits a Seedance 2.5 Spicy First & Last Frame task. Generates a smooth video
        transition between a start and end image (up to 30s), with reduced
        content-safety filtering and bolder, higher-contrast output.

        :param prompt: Text prompt describing the transition and motion.
        :param images_list: Exactly 2 images: [first_frame, last_frame].
        :param resolution: '480p', '720p', '1080p', or '4k'. Price scales with resolution.
        :param duration: Video duration in seconds (4-30).
        :param seed: Random seed for reproducible generation. Use -1 for random.
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :param draft: Generate a cheap 480p draft (resolution must be 480p or omitted).
        :param draft_request_id: Finalize an earlier draft into a full 1080p render.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2.5-spicy-first-last-frame"
        payload = {
            "prompt": prompt,
            "images_list": images_list,
            "resolution": resolution,
            "duration": duration,
            "seed": seed,
            "high_bitrate": high_bitrate,
            "draft": draft,
        }
        if draft_request_id:
            payload["draft_request_id"] = draft_request_id
        return self._post_request(endpoint, payload)

    def omni_reference(self, prompt, images_list=None, videos_list=None, audios_list=None,
                        resolution="720p", duration=5, aspect_ratio="16:9",
                        omni_reference_task_type="auto", seed=-1, high_bitrate=False,
                        draft=False, draft_request_id=None):
        """
        Submits a Seedance 2.5 Spicy Omni Reference task. Blends up to 30 reference
        images, 10 video clips, and 10 audio files into a single guided generation
        (up to 30s), with reduced content-safety filtering.

        :param prompt: Text prompt referencing the images, video clips, and audio as
                       environment, motion, and mood cues.
        :param images_list: Up to 30 reference image URLs.
        :param videos_list: Up to 10 reference video URLs.
        :param audios_list: Up to 10 reference audio URLs.
        :param resolution: '480p', '720p', '1080p', or '4k'. Price scales with resolution.
        :param duration: Video duration in seconds (4-30).
        :param aspect_ratio: 'adaptive', '16:9', '9:16', '1:1', '4:3', '3:4', '21:9', or '9:21'.
        :param omni_reference_task_type: 'auto', 'reference', 'edit', or 'extend'. 'edit'
                       and 'extend' require aspect_ratio='adaptive' ('edit' also
                       requires duration=-1).
        :param seed: Random seed for reproducible generation. Use -1 for random.
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :param draft: Generate a cheap 480p draft (resolution must be 480p or omitted).
        :param draft_request_id: Finalize an earlier draft into a full 1080p render.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2.5-spicy-omni-reference"
        payload = {
            "prompt": prompt,
            "resolution": resolution,
            "duration": duration,
            "aspect_ratio": aspect_ratio,
            "omni_reference_task_type": omni_reference_task_type,
            "seed": seed,
            "high_bitrate": high_bitrate,
            "draft": draft,
        }
        if images_list:
            payload["images_list"] = images_list
        if videos_list:
            payload["videos_list"] = videos_list
        if audios_list:
            payload["audios_list"] = audios_list
        if draft_request_id:
            payload["draft_request_id"] = draft_request_id
        return self._post_request(endpoint, payload)

    def video_edit(self, prompt, video_url, images_list=None, audios_list=None,
                    resolution="720p", duration=5, generate_audio=True, seed=-1,
                    high_bitrate=False):
        """
        Submits a Seedance 2.5 Spicy Video Edit task. Edits an input video from a
        natural-language prompt — the reference video drives subject identity,
        composition, and motion while the model rewrites lighting, style, weather,
        environment, or specific elements as instructed.

        :param prompt: Instructions for the edit. Automatically prefixed with
                       "Edit the input video."
        :param video_url: URL of the video to edit. Videos longer than 30s are trimmed to 30s.
        :param images_list: Up to 30 reference image URLs guiding subject identity or style.
        :param audios_list: Up to 10 reference audio URLs guiding audio generation.
        :param resolution: '480p', '720p', '1080p', or '4k'. Price scales with resolution.
        :param duration: Video duration in seconds (4-30).
        :param generate_audio: If false, the input video's original audio is preserved.
        :param seed: Random seed for reproducible generation. Use -1 for random.
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2.5-spicy-video-edit"
        payload = {
            "prompt": prompt,
            "video_url": video_url,
            "resolution": resolution,
            "duration": duration,
            "generate_audio": generate_audio,
            "seed": seed,
            "high_bitrate": high_bitrate,
        }
        if images_list:
            payload["images_list"] = images_list
        if audios_list:
            payload["audios_list"] = audios_list
        return self._post_request(endpoint, payload)

    def video_extend(self, prompt, video_url, last_image=None, resolution="720p", duration=5,
                      generate_audio=True, seed=-1, high_bitrate=False):
        """
        Submits a Seedance 2.5 Spicy Video Extend task. Extends an input video with a
        new cinematic continuation generated from its last frame and a
        natural-language prompt.

        :param prompt: Desired cinematic continuation — action, camera movement,
                       lighting, mood.
        :param video_url: URL of the video to extend. Generation continues from its last frame.
        :param last_image: Optional target frame URL to interpolate toward.
        :param resolution: '480p', '720p', '1080p', or '4k'. Price scales with resolution.
        :param duration: Length of the extension clip in seconds (4-30).
        :param generate_audio: Whether to generate synchronized audio for the new segment.
        :param seed: Random seed for reproducible generation. Use -1 for random.
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2.5-spicy-video-extend"
        payload = {
            "prompt": prompt,
            "video_url": video_url,
            "resolution": resolution,
            "duration": duration,
            "generate_audio": generate_audio,
            "seed": seed,
            "high_bitrate": high_bitrate,
        }
        if last_image:
            payload["last_image"] = last_image
        return self._post_request(endpoint, payload)

    def motion_control(self, video_url, images_list=None, prompt=None, aspect_ratio="16:9",
                        duration=5, seed=-1, high_bitrate=False, generate_audio=False):
        """
        Submits a Seedance 2.5 Spicy Motion Control task. Recasts an existing
        performance video with a bolder creative treatment while preserving the
        original motion, choreography, blocking, camera work, and location.

        :param video_url: Reference video whose motion, choreography, blocking, and
                          camera work will be preserved.
        :param images_list: Up to 30 character, location, or style reference images used
                            to recast the performers and environment.
        :param prompt: Optional short creative brief describing the recast and its
                       visual treatment. If omitted, roles are inferred automatically.
        :param aspect_ratio: 'adaptive', '16:9', '9:16', '1:1', '4:3', '3:4', '21:9', or '9:21'.
        :param duration: Video duration in seconds (4-30).
        :param seed: Random seed for reproducible generation. Use -1 for random.
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :param generate_audio: Generate audio (music/SFX) for the recast video. Off by default.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2.5-spicy-motion-control"
        payload = {
            "video_url": video_url,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "seed": seed,
            "high_bitrate": high_bitrate,
            "generate_audio": generate_audio,
        }
        if images_list:
            payload["images_list"] = images_list
        if prompt:
            payload["prompt"] = prompt
        return self._post_request(endpoint, payload)

    def _post_request(self, endpoint, payload):
        response = requests.post(endpoint, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def upload_file(self, file_path):
        """
        Uploads a file (image, video, or audio) to MuAPI for use in generation tasks.

        :param file_path: Path to the local file to upload.
        :return: JSON response from the MuAPI containing the URL of the uploaded file.
        """
        endpoint = f"{self.base_url}/upload_file"

        # Omit Content-Type to let requests set the multipart boundary automatically
        headers = {
            "x-api-key": self.api_key
        }

        with open(file_path, "rb") as file_data:
            files = {"file": file_data}
            response = requests.post(endpoint, headers=headers, files=files)

        response.raise_for_status()
        return response.json()

    def get_result(self, request_id):
        """
        Polls for the result of a generation task.
        """
        endpoint = f"{self.base_url}/predictions/{request_id}/result"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def wait_for_completion(self, request_id, poll_interval=5, timeout=600):
        """
        Waits for the video generation to complete and returns the result.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            result = self.get_result(request_id)
            status = result.get("status")

            if status == "completed":
                return result
            elif status == "failed":
                raise Exception(f"Video generation failed: {result.get('error')}")

            print(f"Status: {status}. Waiting {poll_interval} seconds...")
            time.sleep(poll_interval)

        raise TimeoutError("Timed out waiting for video generation to complete.")


if __name__ == "__main__":
    try:
        api = Seedance25SpicyAPI()
        prompt = (
            "A high-contrast, adrenaline-fueled chase through a rain-soaked neon "
            "megacity at night, sparks and shattering glass in slow motion, "
            "aggressive handheld camera energy, exaggerated color grading, 4K cinematic quality."
        )

        print(f"Submitting Seedance 2.5 Spicy T2V task with prompt: {prompt}")
        submission = api.text_to_video(prompt=prompt, duration=5, resolution="1080p")
        request_id = submission.get("request_id")
        print(f"Task submitted. Request ID: {request_id}")

        print("Waiting for completion...")
        result = api.wait_for_completion(request_id)
        print(f"Generation completed! Video URL: {result.get('outputs', [result.get('url')])[0]}")

    except Exception as e:
        print(f"Error: {e}")
