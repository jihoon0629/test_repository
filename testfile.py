from image_filter.custom_image_processor import CustomImageProcessor

input_file = "testimage.jpg"
bmp_file = "testimage_to_24bmp.bmp"

processor = CustomImageProcessor()

processor.auto_convert_to_24bit_bmp(input_file, bmp_file)

processor.apply_grayscale(bmp_file, "example_grayscale.bmp")

processor.apply_invert_colors(bmp_file, "example_inverted.bmp")

processor.apply_pixelation(bmp_file, "example_pixelated.bmp", pixel_size=20)

processor.apply_flip_horizontal(bmp_file, "example_flipped.bmp")

processor.apply_skin_brightness(
    bmp_file,
    "example_brightness.bmp",  # 결과 저장 파일
    brightness_factor=1.3,  # 밝기 증가 비율
    soften_intensity=25,    # 부드러움 추가 강도
)

processor.apply_sepia_tone(bmp_file, "example_sepia.bmp")

processor.apply_neon_filter(bmp_file,"example_neon.bmp", intensity=1.8)

processor.apply_blur(bmp_file, "example_blur.bmp", radius=4)

processor.apply_text_sticker(bmp_file, "example_face.bmp", user_text="Library Test")
