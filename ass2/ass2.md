# Assignment 2

## by Adil Akhmetov

### Question 1.
- a) 
$$
I_k(x,y) = \sum_{i=1}^k \sum_{j=1}^k K_{ij} I (x - i + \frac{k}{2}, y - j + \frac{k}{2})
$$
- b)
$$
I_k(x,y) = \sum_{i=1}^k \sum_{j=1}^k K_{ij} I (x - i + \frac{k}{2}, y - j + \frac{k}{2}) = \\
\sum_{i=1}^k \sum_{j=1}^k g_i h_j I (x - i + \frac{k}{2}, y - j + \frac{k}{2}) = \\
\sum_{j=1}^k h_j \sum_{i=1}^k g_i I (x - i + \frac{k}{2}, y - j + \frac{k}{2}) = \\
\sum_{j=1}^k h_j I (x - i + \frac{k}{2}, y - j + \frac{k}{2}) = \\
I_{gh}(x,y)
$$
- c) For 2D filter since total number of pixels is $N^2$, the number of multiplications is $N^2k^2$ and the number of additions is $N^2(k^2-1)$, the total number of operations is $N^2(2k^2-1)$.  
For 1D filter total of multiplications is $N^2k$ and total of additions is $N^2(k-1)$, the total number of operations is $N^2(2k-1)$. There are 2 1D filters, so the result is $2N^2(2k-1)$  
Differense is $N^2(2k^2-1) - 2N^2(2k-1) = N^2(2k^2-1-4k+2)=N^2(2k^2-4k+1)$

### Question 2.
Following associative property of convolution:
$$
f*g*h=f*(g*h)=(f*g)*h
$$
We say that:
$$
H = [0.25, 0.5, 0.25]\ (column\ vector) \\
H \times H^T = \begin{bmatrix}
  0.625 & 0.125 & 0.625 \\
  0.125 & 0.25 & 0.125 \\
  0.625 & 0.125 & 0.625
  \end{bmatrix}
$$

### Question 3.
Did not understand the topic.

### Question 4.
$$
g(x,y) = \frac{1}{2\pi\sigma^2}e^{-\frac{x^2+y^2}{2\sigma^2}} \\
L(x,y) = \frac{d^2g(x,y)}{dx^2} + \frac{d^2g(x,y)}{dy^2} = \\
\frac{d^2}{dx^2} \frac{1}{2\pi\sigma^2}e^{-\frac{x^2+y^2}{2\sigma^2}} + \frac{d^2}{dy^2} \frac{1}{2\pi\sigma^2}e^{-\frac{x^2+y^2}{2\sigma^2}} = \\
\frac{x^2-\sigma^2}{2\pi\sigma^6}e^{-\frac{x^2+y^2}{2\sigma^2}} + \frac{y^2-\sigma^2}{2\pi\sigma^6}e^{-\frac{x^2+y^2}{2\sigma^2}} = \\
\frac{x^2+y^2-2\sigma^2}{2\pi\sigma^6}e^{-\frac{x^2+y^2}{2\sigma^2}}
$$

### Question 5.
$$
\^{x} = xcos(\theta) - ysin(\theta) \\
\^{y} = xsin(\theta) + ycos(\theta) \\
I_{\^{x}} = \frac{d(\^{x}+\^{y})}{dx} = I_xcos(\theta) + I_ysin(\theta) \\
I_{\^{y}} = \frac{d(\^{x}+\^{y})}{dy} = -I_xsin(\theta) + I_ycos(\theta) \\
\sqrt{I_{x}^2+I_{y}^2} = \sqrt{I_{\^{x}}^2+I_{\^{y}}^2} \\
I_{x}^2+I_{y}^2 = I_{\^{x}}^2+I_{\^{y}}^2 \\
I_{\^{x}}^2+I_{\^{y}}^2 = ((I_xcos(\theta) + I_ysin(\theta))^2 +(-I_xsin(\theta) + I_ycos(\theta))^2 = \\
I_x^2cos^2(\theta) + I_y^2sin^2(\theta) + 2I_xI_ycos(\theta)sin(\theta) + I_x^2sin^2(\theta) + I_y^2cos^2(\theta) - 2I_xI_ycos(\theta)sin(\theta) = \\
I_x^2cos^2(\theta) + I_y^2sin^2(\theta) + I_x^2sin^2(\theta) + I_y^2cos^2(\theta) = \\
I_x^2(cos^2(\theta) + sin^2(\theta)) + I_y^2(cos^2(\theta) + sin^2(\theta)) = \\
I_x^2 + I_y^2
$$

### Question 6.
- a. Use Gaussian filter to get smooth copy, then subtract it from original image
- b. The derivative of Gaussian filter is used for noise suppression, while the difference of Gaussian filter is used for edge detection
- c. Did not understand the topic.