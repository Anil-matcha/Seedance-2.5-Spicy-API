---
name: seedance-2.5-spicy
description: Generate native-4K AI videos with reduced content-safety filtering using Seedance 2.5 Spicy (by ByteDance) — text-to-video, image-to-video, omni reference, video edit/extend, and motion control.
version: 1.0.0
metadata:
  openclaw:
    requires:
      env:
        - MUAPI_API_KEY
      bins:
        - python3.11
    emoji: 🌶️
    homepage: https://muapi.ai
    os: ["macos", "linux"]
---

# Seedance 2.5 Spicy

Seedance 2.5 Spicy is the relaxed-moderation variant of ByteDance's Seedance 2.5 flagship video model, delivered via MuAPI. It generates photorealistic 4K video, up to 30-second clips, and native audio, with reduced content-safety filtering and more dramatic, higher-contrast motion than the standard tier.

## Prerequisites

- **MUAPI_API_KEY**: You must have an API key from [muapi.ai](https://muapi.ai). Set it as an environment variable.

## Usage Guide

### Text-to-Video
```bash
python3.11 skills/seedance-2.5-spicy/seedance_2_5_spicy_cli.py t2v --prompt "A high-contrast, adrenaline-fueled chase through a rain-soaked neon megacity at night" --resolution 1080p --wait
```

### Image-to-Video
```bash
python3.11 skills/seedance-2.5-spicy/seedance_2_5_spicy_cli.py i2v --image_url "https://example.com/scene.jpg" --prompt "Bold, high-energy dolly forward through a neon-drenched alley at night" --wait
```

### First & Last Frame
```bash
python3.11 skills/seedance-2.5-spicy/seedance_2_5_spicy_cli.py first-last-frame --prompt "Create a smooth transition from a cloudy sky to a quiet riverside park path" --images "https://example.com/clouds.jpg" "https://example.com/park.jpg" --wait
```

### Omni-Reference
Condition a video on up to 30 images, 10 video clips, and 10 audio files.
```bash
python3.11 skills/seedance-2.5-spicy/seedance_2_5_spicy_cli.py omni --prompt "Use the images for environment style, the video clips for camera motion" --images "https://example.com/style1.jpg" --videos "https://example.com/motion.mp4" --wait
```

### Video Edit
```bash
python3.11 skills/seedance-2.5-spicy/seedance_2_5_spicy_cli.py video-edit --video_url "https://example.com/input.mp4" --prompt "Change the lighting to golden hour and add light fog to the environment" --wait
```

### Video Extend
```bash
python3.11 skills/seedance-2.5-spicy/seedance_2_5_spicy_cli.py video-extend --video_url "https://example.com/input.mp4" --prompt "The car keeps driving down the coastal road as the sun sets, camera slowly pulling back" --wait
```

### Motion Control
Recast an existing performance video with new performers while preserving motion, camera work, and location.
```bash
python3.11 skills/seedance-2.5-spicy/seedance_2_5_spicy_cli.py motion-control --video_url "https://example.com/dance.mp4" --images "https://example.com/performer1.jpg" --prompt "Recast the dancers with the people in the reference images, bold high-contrast treatment" --wait
```

## Tips for Best Results

- **Be Descriptive**: Detailed, high-contrast prompts get the best results out of the Spicy tier's bolder style.
- **Wait for Completion**: Use `--wait` to receive the final video URL directly. Without it, you get a `request_id` to check later with `status`.
- **Draft Mode**: Pass `--draft` for a cheap 480p preview (t2v/i2v/first-last-frame/omni), then finalize the keeper with `--draft_request_id <id>` for a full-resolution render (draft must be completed and ≤7 days old).
- **Resolution Scales Price**: `--resolution` ranges `480p` → `4k`; 480p is cheapest, 4K is most expensive.
- **Omni Task Type**: `--task_type edit`/`extend` require `--aspect_ratio adaptive` (`edit` also requires `--duration -1`); leave `auto` unless you know the subtype.
- **Durations**: T2V/I2V allow 4-16s; first-last-frame, omni, video-edit, video-extend, and motion-control allow 4-30s.

## Commands Reference

| Command | Arguments | Description |
| :--- | :--- | :--- |
| `t2v` | `--prompt`, `--aspect_ratio`, `--duration`, `--resolution`, `--no_audio`, `--camera_fixed`, `--high_bitrate`, `--draft`, `--draft_request_id`, `--wait` | Text to Video |
| `i2v` | `--prompt`, `--image_url`, `--last_image`, `--duration`, `--resolution`, `--no_audio`, `--camera_fixed`, `--high_bitrate`, `--draft`, `--draft_request_id`, `--wait` | Image to Video |
| `first-last-frame` | `--prompt`, `--images` (2), `--resolution`, `--duration`, `--seed`, `--high_bitrate`, `--draft`, `--draft_request_id`, `--wait` | First & Last Frame transition |
| `omni` | `--prompt`, `--images`, `--videos`, `--audios`, `--resolution`, `--duration`, `--aspect_ratio`, `--task_type`, `--seed`, `--high_bitrate`, `--draft`, `--draft_request_id`, `--wait` | Omni Reference |
| `video-edit` | `--prompt`, `--video_url`, `--images`, `--audios`, `--resolution`, `--duration`, `--no_audio`, `--seed`, `--high_bitrate`, `--wait` | Video Edit |
| `video-extend` | `--prompt`, `--video_url`, `--last_image`, `--resolution`, `--duration`, `--no_audio`, `--seed`, `--high_bitrate`, `--wait` | Video Extend |
| `motion-control` | `--video_url`, `--images`, `--prompt`, `--aspect_ratio`, `--duration`, `--seed`, `--high_bitrate`, `--generate_audio`, `--wait` | Motion Control recast |
| `status` | `--request_id` | Check Task Status |
