# JPEG IMPLEMENTATION

## FONTES:
[JFIF File format](https://www.w3.org/Graphics/JPEG/jfif3.pdf)

[How images are compressed?](https://www.youtube.com/watch?v=Kv1Hiv3ox8I)

[Everything You Need to Know About JPEG](https://www.youtube.com/playlist?list=PLpsTn9TA_Q8VMDyOPrDKmSJYt1DLgDZU4)

[Understanding and Decoding a JPEG Image using Python](https://yasoob.me/posts/understanding-and-writing-jpeg-decoder-in-python/)

[Let's Write a Simple JPEG Library](https://koushtav.me/jpeg/tutorial/2017/11/25lets-write-a-simple-jpeg-library-part-1/)

[Colourspaces (JPEG Pt0)- Computerphile](https://www.youtube.com/watch?v=LFXN9PiOGtY)

Provavelmente voce ja ouviu falar em JPEG. Mas poucas pessoas sabem o que e isso, e ainda menos como ele funciona.

### Encoder
https://github.com/ghallak/jpeg-python/blob/master/encoder.py
https://github.com/fangwei123456/python-jpeg-encoder/blob/master/jpegEncoder.py

### Files examples from:
https://www.learningcontainer.com/sample-bmp-file-for-testing/

---

Algoritmo de compressao.

Explora as caracteristicas da visao humana para manter a informacao de uma imagem ao mesmo tempo diminuir seu espaco de representacao.


### Has 5 major steps
from the video: https://www.youtube.com/watch?v=Kv1Hiv3ox8I
- 1: Color Space Conversion
- 2: Chrominance Downsampling
- 3: Discrete Cosine Transform
- 4: Quantization
- 5: Run Length and Huffman Enconding


## STEP 1: Color Space Conversion
RGB -> YCbCr

Y = 0.299 ∗ R + 0.587 ∗ G + 0.114 ∗ B
Cb = −0.1687 ∗ R −0.3313 ∗ G + 0.5 ∗ B + 128
Cr = 0.5 ∗ R −0.4187 ∗ G −0.0813 ∗ B + 128

## STEP 2: Chroma Subsampling
Uma forma de eliminar redundancia espacial.

https://medium.com/@sddkal/chroma-subsampling-in-numpy-47bf2bb5af83
https://stackoverflow.com/questions/5972698/yuv-subsampling-chroma-channels-in-python

"In the simplest case (no subsampling), each MCU (minimum coded unit) is an 8x8 block of pixels made up of 3 components - Y, Cb, Cr. The image is processed in 8x8 pixel blocks where the 3 color components are separated, passed through a DCT transform and written to the file in the order (Y, Cb, Cr). In all cases of subsampling, the DCT blocks are always composed of 8x8 coefficients or 64 values, but the meaning of those values varies due to the color subsampling."
from: https://stackoverflow.com/questions/35497075/chroma-subsampling-algorithm-for-jpeg