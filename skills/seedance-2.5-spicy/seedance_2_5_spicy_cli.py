import sys
import os
import argparse
import json

# Add the parent directory to the path so we can import the existing Seedance25SpicyAPI
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from seedance_2_5_spicy_api import Seedance25SpicyAPI


def main():
    parser = argparse.ArgumentParser(description="Seedance 2.5 Spicy CLI Wrapper for OpenClaw Skill")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    t2v = subparsers.add_parser("t2v", help="Generate video from text (Spicy)")
    t2v.add_argument("--prompt", required=True, help="Text prompt")
    t2v.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    t2v.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-16)")
    t2v.add_argument("--resolution", default="720p", choices=["480p", "720p", "1080p", "4k"], help="Output resolution")
    t2v.add_argument("--no_audio", action="store_true", help="Disable generated audio")
    t2v.add_argument("--camera_fixed", action="store_true", help="Fix the camera position")
    t2v.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    t2v.add_argument("--draft", action="store_true", help="Generate a cheap 480p draft")
    t2v.add_argument("--draft_request_id", help="Finalize an earlier draft into a full render")
    t2v.add_argument("--wait", action="store_true", help="Wait for completion")

    i2v = subparsers.add_parser("i2v", help="Generate video from image (Spicy)")
    i2v.add_argument("--prompt", required=True, help="Text prompt")
    i2v.add_argument("--image_url", required=True, help="Source image URL")
    i2v.add_argument("--last_image", help="Optional last-frame image URL")
    i2v.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-16)")
    i2v.add_argument("--resolution", default="720p", choices=["480p", "720p", "1080p", "4k"], help="Output resolution")
    i2v.add_argument("--no_audio", action="store_true", help="Disable generated audio")
    i2v.add_argument("--camera_fixed", action="store_true", help="Fix the camera position")
    i2v.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    i2v.add_argument("--draft", action="store_true", help="Generate a cheap 480p draft")
    i2v.add_argument("--draft_request_id", help="Finalize an earlier draft into a full render")
    i2v.add_argument("--wait", action="store_true", help="Wait for completion")

    flf = subparsers.add_parser("first-last-frame", help="Generate a transition between two images (Spicy)")
    flf.add_argument("--prompt", required=True, help="Text prompt describing the transition")
    flf.add_argument("--images", required=True, nargs=2, metavar=("FIRST", "LAST"), help="Exactly 2 image URLs: first_frame last_frame")
    flf.add_argument("--resolution", default="720p", choices=["480p", "720p", "1080p", "4k"], help="Output resolution")
    flf.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-30)")
    flf.add_argument("--seed", type=int, default=-1, help="Random seed (-1 for random)")
    flf.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    flf.add_argument("--draft", action="store_true", help="Generate a cheap 480p draft")
    flf.add_argument("--draft_request_id", help="Finalize an earlier draft into a full render")
    flf.add_argument("--wait", action="store_true", help="Wait for completion")

    omni = subparsers.add_parser("omni", help="Reference-driven generation (Spicy)")
    omni.add_argument("--prompt", required=True, help="Text prompt")
    omni.add_argument("--images", nargs="*", help="Up to 30 reference image URLs")
    omni.add_argument("--videos", nargs="*", help="Up to 10 reference video URLs")
    omni.add_argument("--audios", nargs="*", help="Up to 10 reference audio URLs")
    omni.add_argument("--resolution", default="720p", choices=["480p", "720p", "1080p", "4k"], help="Output resolution")
    omni.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-30)")
    omni.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    omni.add_argument("--task_type", default="auto", choices=["auto", "reference", "edit", "extend"], help="Omni-reference subtask type")
    omni.add_argument("--seed", type=int, default=-1, help="Random seed (-1 for random)")
    omni.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    omni.add_argument("--draft", action="store_true", help="Generate a cheap 480p draft")
    omni.add_argument("--draft_request_id", help="Finalize an earlier draft into a full render")
    omni.add_argument("--wait", action="store_true", help="Wait for completion")

    edit = subparsers.add_parser("video-edit", help="Edit an existing video (Spicy)")
    edit.add_argument("--prompt", required=True, help="Edit instructions")
    edit.add_argument("--video_url", required=True, help="URL of the video to edit")
    edit.add_argument("--images", nargs="*", help="Up to 30 reference image URLs")
    edit.add_argument("--audios", nargs="*", help="Up to 10 reference audio URLs")
    edit.add_argument("--resolution", default="720p", choices=["480p", "720p", "1080p", "4k"], help="Output resolution")
    edit.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-30)")
    edit.add_argument("--no_audio", action="store_true", help="Preserve the input video's original audio")
    edit.add_argument("--seed", type=int, default=-1, help="Random seed (-1 for random)")
    edit.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    edit.add_argument("--wait", action="store_true", help="Wait for completion")

    extend = subparsers.add_parser("video-extend", help="Extend an existing video (Spicy)")
    extend.add_argument("--prompt", required=True, help="Desired cinematic continuation")
    extend.add_argument("--video_url", required=True, help="URL of the video to extend")
    extend.add_argument("--last_image", help="Optional target frame URL")
    extend.add_argument("--resolution", default="720p", choices=["480p", "720p", "1080p", "4k"], help="Output resolution")
    extend.add_argument("--duration", type=int, default=5, help="Extension length in seconds (4-30)")
    extend.add_argument("--no_audio", action="store_true", help="Disable synchronized audio for the new segment")
    extend.add_argument("--seed", type=int, default=-1, help="Random seed (-1 for random)")
    extend.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    extend.add_argument("--wait", action="store_true", help="Wait for completion")

    motion = subparsers.add_parser("motion-control", help="Recast a performance video (Spicy)")
    motion.add_argument("--video_url", required=True, help="Reference video to preserve motion/camera work from")
    motion.add_argument("--images", nargs="*", help="Up to 30 character/location/style reference images")
    motion.add_argument("--prompt", help="Optional creative brief describing the recast")
    motion.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    motion.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-30)")
    motion.add_argument("--seed", type=int, default=-1, help="Random seed (-1 for random)")
    motion.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    motion.add_argument("--generate_audio", action="store_true", help="Generate audio (music/SFX) for the recast video")
    motion.add_argument("--wait", action="store_true", help="Wait for completion")

    status = subparsers.add_parser("status", help="Get task status")
    status.add_argument("--request_id", required=True, help="Request ID")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        api = Seedance25SpicyAPI()

        if args.command == "t2v":
            res = api.text_to_video(args.prompt, args.aspect_ratio, args.duration, args.resolution,
                                     not args.no_audio, args.camera_fixed, args.high_bitrate,
                                     args.draft, args.draft_request_id)
        elif args.command == "i2v":
            res = api.image_to_video(args.prompt, args.image_url, args.last_image, args.duration,
                                      args.resolution, not args.no_audio, args.camera_fixed,
                                      args.high_bitrate, args.draft, args.draft_request_id)
        elif args.command == "first-last-frame":
            res = api.first_last_frame(args.prompt, args.images, args.resolution, args.duration,
                                        args.seed, args.high_bitrate, args.draft, args.draft_request_id)
        elif args.command == "omni":
            res = api.omni_reference(args.prompt, args.images, args.videos, args.audios, args.resolution,
                                      args.duration, args.aspect_ratio, args.task_type, args.seed,
                                      args.high_bitrate, args.draft, args.draft_request_id)
        elif args.command == "video-edit":
            res = api.video_edit(args.prompt, args.video_url, args.images, args.audios, args.resolution,
                                  args.duration, not args.no_audio, args.seed, args.high_bitrate)
        elif args.command == "video-extend":
            res = api.video_extend(args.prompt, args.video_url, args.last_image, args.resolution,
                                    args.duration, not args.no_audio, args.seed, args.high_bitrate)
        elif args.command == "motion-control":
            res = api.motion_control(args.video_url, args.images, args.prompt, args.aspect_ratio,
                                      args.duration, args.seed, args.high_bitrate, args.generate_audio)
        elif args.command == "status":
            res = api.get_result(args.request_id)
            print(json.dumps(res, indent=2))
            return

        request_id = res.get("request_id")

        if args.wait and request_id:
            print(f"Task submitted: {request_id}. Waiting for completion...")
            result = api.wait_for_completion(request_id)
            print(json.dumps(result, indent=2))
        else:
            print(json.dumps(res, indent=2))

    except Exception as e:
        print(json.dumps({"error": str(e)}, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
