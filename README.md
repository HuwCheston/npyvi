# npyvi
> Python implementation of normalised pairwise variability index (nPVI), as defined in Grabe & Low (2002)

The normalised pairwise variability index (nPVI) is a measure of the average variation of a set of durations, ordered by
successive pairs. First conceived for the rhythmic classification of speech by Grabe & Low (2002), nPVI has since also
been utilised in music perception and cognition research, e.g. Toussaint (2012). 

While a previous implementation of nPVI does exist for MATLAB (Livingstone 2011), Python is more commonly used by 
researchers in the above fields. The implementation provided here is incredibly simple and does not require the 
installation of any additional packages beyond those within the standard Python 3+ library.

## Installation
TODO

## Usage

    from npyvi import npvi
    
    # Calculating nPVI for a single array
    >>> npvi(1, 2, 3)
    53.333333333333336

    # Calculating nPVI seperately for multiple arrays
    >>> npvi([1, 2, 3], [3, 3, 6], [4, 6, 8])
    [53.333333333333336, 33.33333333333333, 34.285714285714285]

## References
- Grabe, E., & Low, E. L. (2002). Durational variability in speech and the rhythm class hypothesis. In C. Gussenhoven & 
N. Warner (Eds.), Papers in laboratory psychology (pp. 515–546). Cambridge University Press.
- Livingstone, L. (2011). [Normalized Pairwise Variability Index](https://www.mathworks.com/matlabcentral/fileexchange/33098-normalized-pairwise-variability-index)
MATLAB Central File Exchange. Retrieved October 30, 2022.
- Toussaint, G. T. (2012). The Pairwise Variability Index as a Tool in Musical Rhythm Analysis. In E. Cambouropoulos, 
C. Tsougras, P. Mavromatis, & K. Pastiadis (Eds.), Proceedings of the 12th International Conference on Music Perception 
and Cognition and the 8th Triennial Conference of the European Society for the Cognitive Sciences of Music 
(pp. 1001–1008).

## Meta
Huw Cheston – [@HuwCheston](https://twitter.com/huwcheston) – hwc31@cam.ac.uk

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/huwcheston/npyvi](https://github.com/huwcheston/npyvi/)
