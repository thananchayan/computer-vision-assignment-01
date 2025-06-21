def reduce_intensity_levels(image, levels):
    factor = 256 // levels
    return (image // factor) * factor
