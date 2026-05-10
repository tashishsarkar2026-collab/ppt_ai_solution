# """
# This file reads PowerPoint (.pptx) files
# and converts all slide objects into structured Python data.

# Goal:
# Make PowerPoint understandable for machines.
# """

# from pptx import Presentation


# # PowerPoint uses EMU internally.
# # We convert it into inches for readability.
# EMU_TO_INCH = 914400


# class PPTExtractor:
#     """
#     Main extractor class.

#     Responsibilities:
#     - Open PPTX
#     - Read slides
#     - Read shapes
#     - Recursively inspect grouped objects
#     """

#     def __init__(self, ppt_path):
#         """
#         Initialize presentation.

#         Example:
#         templates/curated/project-management-infographics.pptx
#         """

#         self.prs = Presentation(ppt_path)

#     def extract_shape(self, shape, shape_index):
#         """
#         Extract a single shape.

#         If shape is a GROUP,
#         recursively extract inner shapes too.
#         """

#         shape_data = {
#             "shape_index": shape_index,
#             "shape_name": shape.name,
#             "shape_type": str(shape.shape_type),

#             "x": shape.left / EMU_TO_INCH,
#             "y": shape.top / EMU_TO_INCH,
#             "width": shape.width / EMU_TO_INCH,
#             "height": shape.height / EMU_TO_INCH,

#             "text": "",

#             # Nested shapes inside GROUP objects
#             "children": []
#         }

#         # Extract text if available
#         if hasattr(shape, "text"):
#             shape_data["text"] = shape.text

#         """
#         GROUP shapes contain inner shapes.

#         Example:
#         timeline block
#             ├── icon
#             ├── title
#             ├── description
#         """

#         if "GROUP" in str(shape.shape_type):

#             for child_index, child_shape in enumerate(shape.shapes):

#                 child_data = self.extract_shape(
#                     child_shape,
#                     child_index
#                 )

#                 shape_data["children"].append(child_data)

#         return shape_data

#     def extract(self):
#         """
#         Extract all slides and shapes.
#         """

#         all_slides = []

#         # Loop through all slides
#         for slide_index, slide in enumerate(self.prs.slides):

#             slide_data = {
#                 "slide_index": slide_index,
#                 "shapes": []
#             }

#             # Loop through all shapes
#             for shape_index, shape in enumerate(slide.shapes):

#                 # Recursive extraction
#                 shape_data = self.extract_shape(
#                     shape,
#                     shape_index
#                 )

#                 slide_data["shapes"].append(shape_data)

#             all_slides.append(slide_data)

#         return all_slides


def extract(
    self,
    progress_bar=None,
    status_text=None
):
    """
    Extract all slides and shapes.

    Supports:
    - Streamlit progress bar
    - Human-readable extraction status
    """

    all_slides = []

    total_slides = len(self.prs.slides)

    print(f"\nTotal Slides Found: {total_slides}\n")

    # Loop through all slides
    for slide_index, slide in enumerate(self.prs.slides):

        # Progress %
        progress = int(
            ((slide_index + 1) / total_slides) * 100
        )

        # Streamlit progress bar
        if progress_bar:
            progress_bar.progress(progress)

        # Streamlit status text
        if status_text:
            status_text.text(
                (
                    f"Extracting Slide "
                    f"{slide_index + 1} "
                    f"of {total_slides}"
                )
            )

        # Console logs
        print(
            f"[INFO] Processing Slide "
            f"{slide_index + 1}/{total_slides}"
        )

        slide_data = {
            "slide_index": slide_index,
            "shapes": []
        }

        infographic_count = 0

        # Loop through shapes
        for shape_index, shape in enumerate(slide.shapes):

            shape_data = self.extract_shape(
                shape,
                shape_index
            )

            slide_data["shapes"].append(shape_data)

            # Detect infographic/group objects
            if "GROUP" in shape_data["shape_type"]:
                infographic_count += 1

        print(
            f"[INFO] Infographics detected: "
            f"{infographic_count}"
        )

        all_slides.append(slide_data)

    print("\n[INFO] Extraction Completed\n")

    return all_slides