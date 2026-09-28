# Seedance 2.5 Spicy API: Python Wrapper for ByteDance's Relaxed-Moderation AI Video Generator

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNHYtNGgtMnYtMmg0djZoLTJ6bTAtOFY2aDJ2MmgtMnoiLz48L3N2Zz4=)](https://muapi.ai?utm_source=github&utm_medium=badge&utm_campaign=seedance-2.5-spicy-api)

[![PyPI version](https://img.shields.io/pypi/v/seedance-2-5-spicy-api.svg)](https://pypi.org/project/seedance-2-5-spicy-api/)
[![GitHub stars](https://img.shields.io/github/stars/Anil-matcha/Seedance-2.5-Spicy-API.svg)](https://github.com/Anil-matcha/Seedance-2.5-Spicy-API/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

The most comprehensive Python wrapper for the **Seedance 2.5 Spicy API** (developed by ByteDance), delivered via [muapi.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2.5-spicy-api). Seedance 2.5 Spicy is the relaxed-moderation variant of the [Seedance 2.5](https://github.com/Anil-matcha/Seedance-2-API) flagship model — native 4K, up to 30-second clips, native audio, and precise camera trajectory control, with **reduced content-safety filtering** and more dramatic, higher-contrast motion than the standard tier.

> ⚠️ **Content policy notice**: "Spicy" means reduced automated content-safety filtering, not an anything-goes endpoint. Generated content still must comply with MuAPI's and the underlying provider's terms of service and applicable law. Do not use this API to generate content involving minors, non-consensual imagery, or other prohibited material.

## Related Projects

- [Seedance-2-API](https://github.com/Anil-matcha/Seedance-2-API) — Python wrapper for the standard-moderation Seedance 2.0, 2.5, and 2 Mini API.
- [Seedance-2-Spicy-API](https://github.com/Anil-matcha/Seedance-2-Spicy-API) — Python SDK and MCP server for the Seedance 2 Spicy tier.
- [Wan-3.0-Spicy-API](https://github.com/Anil-matcha/Wan-3.0-Spicy-API) — Python SDK and MCP server for the Wan 3.0 Spicy tier.
- [Seedance-3-API](https://github.com/Anil-matcha/Seedance-3-API) — companion project for the next Seedance API generation on MuAPI.
- [seedance-2.5-mcp](https://github.com/Anil-matcha/seedance-2.5-mcp) — Focused MCP server for Seedance 2.5 Preview with 720p/480p route selection.
- [seedance2.5-comfyui](https://github.com/Anil-matcha/seedance2.5-comfyui) — Native Seedance 2.5 ComfyUI custom nodes and example workflows.
- [awesome-seedance-2.5-api-prompts](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts) — Curated Seedance 2.5 API guide, prompts, camera controls, and video generation examples.
- [awesome-seedance-motion-control-api](https://github.com/Anil-matcha/awesome-seedance-motion-control-api) — Seedance 2 & 2.5 Motion Control API guide.

## 🚀 Why Use Seedance 2.5 Spicy API?

- **Relaxed Content Filtering**: Broader creative range than the standard Seedance 2.5 tier, while keeping the same underlying model quality.
- **Native 4K**: Photorealistic 4K output on nearly every endpoint (price scales with resolution).
- **Extended Clips**: Up to 30-second generations on Omni Reference, First & Last Frame, Video Edit, Video Extend, and Motion Control.
- **Native Audio**: Synchronized audio generated alongside the video (toggleable).
- **Draft Mode**: Generate a cheap 480p draft first, then finalize the keeper at full resolution without re-submitting the whole prompt.
- **Omni-Reference**: Blend up to 30 images, 10 video clips, and 10 audio files into a single guided generation.
- **Motion Control**: Recast an existing performance video with new performers while preserving the original motion, choreography, blocking, and camera work.

## 🌟 Key Features

- ✅ **Text-to-Video**: Photorealistic 4K video directly from a text prompt.
- ✅ **Image-to-Video**: Animate a single image, with optional first-last frame control.
- ✅ **First & Last Frame**: Smooth transition between a start and end image, up to 30s.
- ✅ **Omni-Reference**: Multi-modal generation from up to 30 images, 10 videos, and 10 audio references.
- ✅ **Video Edit**: Rewrite lighting, style, weather, or elements of an existing video via natural-language instructions.
- ✅ **Video Extend**: Generate a cinematic continuation from a video's last frame.
- ✅ **Motion Control**: Recast a performance video's performers/environment while preserving motion and camera work.
- ✅ **Draft → Finalize Workflow**: Cheap 480p drafts finalized to 1080p+ without resubmitting prompts/media.
- ✅ **File Upload**: Upload local images/videos/audio directly via `upload_file()`.

---

## 🛠 Installation

### Via Pip (Recommended)
```bash
pip install seedance-2-5-spicy-api
```

### From Source
```bash
git clone https://github.com/Anil-matcha/Seedance-2.5-Spicy-API.git
cd Seedance-2.5-Spicy-API
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the root directory and add your [MuAPI](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2.5-spicy-api) API key:
```env
MUAPI_API_KEY=your_muapi_api_key_here
```

---

## 🤖 Seedance 2.5 Spicy MCP Server

Use Seedance 2.5 Spicy as an **MCP (Model Context Protocol)** server so AI assistants (Claude Desktop, Cursor, etc.) can invoke the tools directly.

```bash
python3 mcp_server.py
```

Test with the MCP Inspector:
```bash
npx -y @modelcontextprotocol/inspector python3 mcp_server.py
```

---

## 💻 Quick Start (Python)

```python
from seedance_2_5_spicy_api import Seedance25SpicyAPI

api = Seedance25SpicyAPI()

# Text-to-Video (Spicy)
submission = api.text_to_video(
    prompt="A high-contrast, adrenaline-fueled chase through a rain-soaked neon megacity at night, "
           "sparks and shattering glass in slow motion, aggressive handheld camera energy, 4K cinematic quality",
    resolution="1080p",
    duration=5,
)
result = api.wait_for_completion(submission["request_id"])
print(f"Video: {result['outputs'][0]}")
```

---

## 📡 API Endpoints & Reference

### 1. Seedance 2.5 Spicy Text-to-Video
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2.5-spicy-text-to-video`

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | Spicy mode favors bolder, higher-contrast, more expressive results. |
| `aspect_ratio` | enum | No | `16:9` | `adaptive`, `16:9`, `9:16`, `1:1`, `3:4`, `4:3`, `21:9` |
| `resolution` | enum | No | `720p` | `480p`, `720p`, `1080p`, `4k` — price scales with resolution |
| `duration` | int | No | `5` | Seconds (4-16) |
| `generate_audio` | boolean | No | `true` | Whether to generate audio for the video |
| `camera_fixed` | boolean | No | `false` | Whether to fix the camera position |
| `high_bitrate` | boolean | No | `false` | Higher visual fidelity, larger files |
| `draft` | boolean | No | `false` | Generate a cheap 480p draft |
| `draft_request_id` | string | No | — | Finalize an earlier draft into a full render |

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.5-spicy-text-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A high-contrast, adrenaline-fueled chase through a rain-soaked neon megacity at night, 4K cinematic quality",
      "resolution": "1080p",
      "duration": 5
  }'
```

### 2. Seedance 2.5 Spicy Image-to-Video
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2.5-spicy-image-to-video`

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | Describes the video motion and style. |
| `image_url` | string | Yes | — | URL of the input image to animate into video. |
| `last_image` | string | No | — | Optional last frame image for first-last frame control. |
| `resolution` | enum | No | `720p` | `480p`, `720p`, `1080p`, `4k` |
| `duration` | int | No | `5` | Seconds (4-16) |
| `generate_audio` | boolean | No | `true` | Whether to generate audio for the video |
| `camera_fixed` | boolean | No | `false` | Whether to fix the camera position |
| `high_bitrate` | boolean | No | `false` | Higher visual fidelity, larger files |
| `draft` / `draft_request_id` | boolean / string | No | — | Draft → finalize workflow |

### 3. Seedance 2.5 Spicy First & Last Frame
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2.5-spicy-first-last-frame`

Generates a smooth video transition between a start and end image, up to 30 seconds.

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | Describes the transition and motion. |
| `images_list` | array[string] | Yes | — | Exactly 2 images: `[first_frame, last_frame]`. |
| `resolution` | enum | No | `720p` | `480p`, `720p`, `1080p`, `4k` |
| `duration` | int | No | `5` | Seconds (4-30) |
| `seed` | int | No | `-1` | Random seed; `-1` for random |
| `high_bitrate` | boolean | No | `false` | Higher visual fidelity, larger files |
| `draft` / `draft_request_id` | boolean / string | No | — | Draft → finalize workflow |

### 4. Seedance 2.5 Spicy Omni Reference
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2.5-spicy-omni-reference`

Blends reference images, video clips, and audio into a single guided generation, up to 30 seconds.

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | References the images/videos/audio as environment, motion, and mood cues. |
| `images_list` | array[string] | No | — | Up to 30 reference image URLs. |
| `videos_list` | array[string] | No | — | Up to 10 reference video URLs. |
| `audios_list` | array[string] | No | — | Up to 10 reference audio URLs. |
| `resolution` | enum | No | `720p` | `480p`, `720p`, `1080p`, `4k` |
| `duration` | int | No | `5` | Seconds (4-30) |
| `aspect_ratio` | enum | No | `16:9` | `adaptive`, `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `9:21` |
| `omni_reference_task_type` | enum | No | `auto` | `auto`, `reference`, `edit`, `extend` — `edit`/`extend` require `aspect_ratio=adaptive` (`edit` also requires `duration=-1`) |
| `seed` | int | No | `-1` | Random seed; `-1` for random |
| `high_bitrate` | boolean | No | `false` | Higher visual fidelity, larger files |
| `draft` / `draft_request_id` | boolean / string | No | — | Draft → finalize workflow |

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.5-spicy-omni-reference" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "Create a calm cinematic park sequence using the images for environment style and the video clips for camera motion",
      "images_list": ["https://example.com/style1.jpg"],
      "videos_list": ["https://example.com/motion.mp4"]
  }'
```

### 5. Seedance 2.5 Spicy Video Edit
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2.5-spicy-video-edit`

Edits an input video from a natural-language prompt; the reference video drives subject identity, composition, and motion.

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | Automatically prefixed with "Edit the input video." |
| `video_url` | string | Yes | — | Video to edit; videos longer than 30s are trimmed to 30s. |
| `images_list` | array[string] | No | — | Up to 30 reference image URLs guiding subject identity/style. |
| `audios_list` | array[string] | No | — | Up to 10 reference audio URLs. |
| `resolution` | enum | No | `720p` | `480p`, `720p`, `1080p`, `4k` |
| `duration` | int | No | `5` | Seconds (4-30) |
| `generate_audio` | boolean | No | `true` | If false, the input video's original audio is preserved. |
| `seed` | int | No | `-1` | Random seed; `-1` for random |
| `high_bitrate` | boolean | No | `false` | Higher visual fidelity, larger files |

### 6. Seedance 2.5 Spicy Video Extend
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2.5-spicy-video-extend`

Extends an input video with a new cinematic continuation generated from its last frame.

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | Desired cinematic continuation — action, camera movement, lighting, mood. |
| `video_url` | string | Yes | — | Generation continues from this video's last frame. |
| `last_image` | string | No | — | Optional target frame to interpolate toward. |
| `resolution` | enum | No | `720p` | `480p`, `720p`, `1080p`, `4k` |
| `duration` | int | No | `5` | Extension length in seconds (4-30) |
| `generate_audio` | boolean | No | `true` | Whether to generate synchronized audio for the new segment |
| `seed` | int | No | `-1` | Random seed; `-1` for random |
| `high_bitrate` | boolean | No | `false` | Higher visual fidelity, larger files |

### 7. Seedance 2.5 Spicy Motion Control
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2.5-spicy-motion-control`

Recasts an existing performance video with a bolder creative treatment while preserving the original motion, choreography, blocking, camera work, and location.

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `video_url` | string | Yes | — | Reference video whose motion/choreography/camera work is preserved. |
| `images_list` | array[string] | No | — | Up to 30 character, location, or style reference images. |
| `prompt` | string | No | — | Optional creative brief; roles are inferred automatically if omitted. |
| `aspect_ratio` | enum | No | `16:9` | `adaptive`, `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `9:21` |
| `duration` | int | No | `5` | Seconds (4-30) |
| `seed` | int | No | `-1` | Random seed; `-1` for random |
| `high_bitrate` | boolean | No | `false` | Higher visual fidelity, larger files |
| `generate_audio` | boolean | No | `false` | Generate audio (music/SFX) for the recast video; off by default. |

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2.5-spicy-motion-control" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "video_url": "https://example.com/dance.mp4",
      "images_list": ["https://example.com/performer1.jpg"],
      "prompt": "Recast the dancers with the people in the reference images and use a bold, high-contrast visual treatment"
  }'
```

---

## 💰 Pricing

| Endpoint | Cost |
|---|---|
| Seedance 2.5 Spicy Text-to-Video | $0.60 / generation (scales with resolution) |
| Seedance 2.5 Spicy Image-to-Video | $0.60 / generation (scales with resolution) |
| Seedance 2.5 Spicy First & Last Frame | $1.87 / generation (scales with resolution) |
| Seedance 2.5 Spicy Omni Reference | $1.87 / generation (scales with resolution) |
| Seedance 2.5 Spicy Video Edit | $1.87 / generation (scales with resolution) |
| Seedance 2.5 Spicy Video Extend | $1.87 / generation (scales with resolution) |
| Seedance 2.5 Spicy Motion Control | $1.65 / generation |

Pricing is illustrative and subject to change — check [muapi.ai/seedance-2.5-spicy](https://muapi.ai/seedance-2.5-spicy?utm_source=github&utm_medium=readme&utm_campaign=seedance-2.5-spicy-api) for current rates.

---

## 📖 Method Reference

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `text_to_video` | `prompt`, `aspect_ratio`, `duration`, `resolution`, `generate_audio`, `camera_fixed`, `high_bitrate`, `draft`, `draft_request_id` | Text to Video. |
| `image_to_video` | `prompt`, `image_url`, `last_image`, `duration`, `resolution`, `generate_audio`, `camera_fixed`, `high_bitrate`, `draft`, `draft_request_id` | Image to Video. |
| `first_last_frame` | `prompt`, `images_list`, `resolution`, `duration`, `seed`, `high_bitrate`, `draft`, `draft_request_id` | First & Last Frame transition. |
| `omni_reference` | `prompt`, `images_list`, `videos_list`, `audios_list`, `resolution`, `duration`, `aspect_ratio`, `omni_reference_task_type`, `seed`, `high_bitrate`, `draft`, `draft_request_id` | Omni Reference. |
| `video_edit` | `prompt`, `video_url`, `images_list`, `audios_list`, `resolution`, `duration`, `generate_audio`, `seed`, `high_bitrate` | Video Edit. |
| `video_extend` | `prompt`, `video_url`, `last_image`, `resolution`, `duration`, `generate_audio`, `seed`, `high_bitrate` | Video Extend. |
| `motion_control` | `video_url`, `images_list`, `prompt`, `aspect_ratio`, `duration`, `seed`, `high_bitrate`, `generate_audio` | Motion Control recast. |
| `upload_file` | `file_path` | Upload a local file (image, video, or audio) to MuAPI. |
| `get_result` | `request_id` | Check task status. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper for generation tasks. |

---

## 🔗 Official Resources
- **Landing page**: [Seedance 2.5 Spicy on MuAPI](https://muapi.ai/seedance-2.5-spicy?utm_source=github&utm_medium=readme&utm_campaign=seedance-2.5-spicy-api)
- **Playground**: [Text-to-Video](https://muapi.ai/playground/seedance-2.5-spicy-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2.5-spicy-api) · [Image-to-Video](https://muapi.ai/playground/seedance-2.5-spicy-image-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2.5-spicy-api)
- **Access Keys**: [muapi.ai/access-keys](https://muapi.ai/access-keys?utm_source=github&utm_medium=readme&utm_campaign=seedance-2.5-spicy-api)
- **API Reference**: [muapi.ai/docs/api-reference](https://muapi.ai/docs/api-reference?utm_source=github&utm_medium=readme&utm_campaign=seedance-2.5-spicy-api)
- **API Provider**: [MuAPI.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2.5-spicy-api)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: Seedance 2.5 Spicy API, ByteDance Seedance 2.5 Spicy, uncensored AI video generator, relaxed content moderation video API, native 4K video generation, Text-to-Video AI, Image-to-Video API, Omni Reference video generation, Video Edit API, Video Extend API, Motion Control API, Seedance Python SDK, Sora Alternative, MuAPI, Video Generation API, Cinematic AI Video, Python Video API.
