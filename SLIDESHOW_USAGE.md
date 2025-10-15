# Banner Slideshow Feature

The banner on your Jekyll site now supports automatic image slideshow functionality with smooth fade transitions.

## How to Use

### Basic Setup

To enable the slideshow on any page, add the following to your page's front matter:

```yaml
---
layout: about
title: Your Page Title
banner: "/assets/images/banners/default.jpg"  # Fallback image
banner_slideshow:
  - "/assets/images/banners/image1.jpg"
  - "/assets/images/banners/image2.jpg"
  - "/assets/images/banners/image3.jpg"
  - "/assets/images/banners/image4.jpg"
banner_slideshow_interval: 5000  # Time in milliseconds (optional, default: 5000)
---
```

### Parameters

- **`banner`** (optional): Fallback banner image when slideshow is not used or as a reference
- **`banner_slideshow`** (required): Array of image paths for the slideshow
- **`banner_slideshow_interval`** (optional): Time between slide transitions in milliseconds (default: 5000ms / 5 seconds)

### Example Configurations

#### Fast Slideshow (3 seconds)
```yaml
banner_slideshow:
  - "/assets/images/banners/slide1.jpg"
  - "/assets/images/banners/slide2.jpg"
banner_slideshow_interval: 3000
```

#### Slow Slideshow (10 seconds)
```yaml
banner_slideshow:
  - "/assets/images/banners/slide1.jpg"
  - "/assets/images/banners/slide2.jpg"
  - "/assets/images/banners/slide3.jpg"
banner_slideshow_interval: 10000
```

## Features

- **Smooth Transitions**: 1-second fade effect between slides
- **Automatic Cycling**: Slides automatically advance at the specified interval
- **Backward Compatible**: Pages without `banner_slideshow` will display a single banner as before
- **Minimum Requirement**: At least 2 images required for slideshow (with 1 image, it displays as a static banner)
- **Responsive**: Works on all screen sizes

## Adding Your Own Images

1. Place your banner images in `/assets/images/banners/`
2. Recommended image specifications:
   - Resolution: 1920x560 pixels (or similar aspect ratio)
   - Format: JPEG or PNG
   - File size: Keep under 500KB for optimal loading

3. Update the `banner_slideshow` array in your page's front matter with the new image paths

## Customization

### Changing Transition Duration

The CSS transition is currently set to 1 second. To modify this, edit `_includes/views/banner.html` and change:

```css
transition: opacity 1s ease-in-out;
```

To your preferred duration (e.g., `2s` for 2 seconds).

### Changing Transition Effect

The current implementation uses opacity-based fade transitions. The transition effect is defined in the inline styles within `_includes/views/banner.html`.

## Technical Details

- The slideshow is implemented using pure JavaScript and CSS
- No external dependencies required
- JavaScript is automatically injected only when `banner_slideshow` is present
- CSS animations use GPU-accelerated opacity transitions for smooth performance

## Troubleshooting

**Slideshow not working?**
- Ensure you have at least 2 images in the `banner_slideshow` array
- Check that image paths are correct and start with `/`
- Verify images exist in the specified location

**Images not loading?**
- Check file paths are correct relative to your site root
- Ensure image files are committed to your repository
- Verify file permissions allow reading the images

**Transition looks choppy?**
- Large image files may cause performance issues
- Optimize your images (compress, resize) before using them
- Consider using a CDN for faster image delivery
