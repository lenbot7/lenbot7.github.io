# Image Slideshow Feature

Your Jekyll site now supports automatic image slideshow functionality that can be added to page content with smooth fade transitions.

## How to Use

### Basic Setup

To add a slideshow to any page content, include the HTML, CSS, and JavaScript directly in your page:

```html
---
layout: about
title: Your Page Title
banner: "/assets/images/banners/default.jpg"
---

<h2>Your Content Title</h2>

<div class="content-slideshow">
  <div class="content-slideshow-container">
    <div class="content-slide active" style="background-image: url(/assets/images/banners/image1.jpg)"></div>
    <div class="content-slide" style="background-image: url(/assets/images/banners/image2.jpg)"></div>
    <div class="content-slide" style="background-image: url(/assets/images/banners/image3.jpg)"></div>
    <div class="content-slide" style="background-image: url(/assets/images/banners/image4.jpg)"></div>
  </div>
</div>

<style>
  .content-slideshow {
    width: 100%;
    margin: 20px 0;
    overflow: hidden;
  }
  
  .content-slideshow-container {
    position: relative;
    width: 100%;
    height: 400px;
    background-color: #333;
  }
  
  .content-slide {
    position: absolute;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    opacity: 0;
    transition: opacity 1s ease-in-out;
  }
  
  .content-slide.active {
    opacity: 1;
  }
</style>

<script>
  (function() {
    var slides = document.querySelectorAll('.content-slide');
    var currentSlide = 0;
    var interval = 5000; // 5 seconds
    
    function nextSlide() {
      slides[currentSlide].classList.remove('active');
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add('active');
    }
    
    if (slides.length > 1) {
      setInterval(nextSlide, interval);
    }
  })();
</script>

<p>Your other content here</p>
```

### Customization Options

#### Change Slideshow Height
Modify the `height` property in the CSS:
```css
.content-slideshow-container {
  height: 500px;  /* Change from 400px to your preferred height */
}
```

#### Change Transition Speed
Modify the `interval` variable in the JavaScript (in milliseconds):
```javascript
var interval = 3000; // 3 seconds (faster)
var interval = 10000; // 10 seconds (slower)
```

#### Change Fade Duration
Modify the `transition` property in the CSS:
```css
.content-slide {
  transition: opacity 2s ease-in-out;  /* Change from 1s to 2s */
}
```

## Features

- **Smooth Transitions**: 1-second fade effect between slides
- **Automatic Cycling**: Slides automatically advance at the specified interval (default: 5 seconds)
- **Flexible Placement**: Can be added anywhere in your page content
- **Customizable**: Easy to adjust height, timing, and transition effects
- **Responsive**: Works on all screen sizes
- **Pure JavaScript/CSS**: No external dependencies required

## Adding Your Own Images

1. Place your images in `/assets/images/banners/` or any other assets directory
2. Add `<div>` elements for each image in the slideshow container:
   ```html
   <div class="content-slide" style="background-image: url(/path/to/your/image.jpg)"></div>
   ```
3. Make sure the first slide has the `active` class
4. Recommended image specifications:
   - Resolution: 1920x400 pixels (or similar 16:9 aspect ratio)
   - Format: JPEG or PNG
   - File size: Keep under 500KB for optimal loading

## Technical Details

- The slideshow uses opacity-based transitions for smooth animations
- JavaScript automatically cycles through slides using `setInterval`
- CSS transitions use GPU-accelerated opacity for optimal performance
- The first slide is shown immediately on page load

## Troubleshooting

**Slideshow not advancing?**
- Check browser console for JavaScript errors
- Ensure the script is properly closed with `</script>`
- Verify you have multiple slides defined

**Images not loading?**
- Check file paths are correct (use absolute paths starting with `/`)
- Ensure image files exist in the specified location
- Verify file permissions allow reading the images

**Transition looks choppy?**
- Large image files may cause performance issues
- Optimize your images (compress, resize) before using them
- Consider using WebP format for better compression

**Only one image shows?**
- Make sure the first slide has the `active` class
- Check that all other slides don't have the `active` class
- Verify CSS is properly closed with `</style>`
