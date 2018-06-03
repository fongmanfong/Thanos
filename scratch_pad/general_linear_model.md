# General Linear Model & Regression


#### How are regression, the t-test, and the ANOVA all versions of the general linear model?

Regression: ![](http://latex.codecogs.com/svg.latex?Y%20%3D%20%5Cbeta_%7B0%7D%20&plus;%20%5Cbeta_%7B1%7DX_%7Bcontinious%7D%20&plus;%20%5Cvarepsilon)

t-test: ![](http://latex.codecogs.com/svg.latex?Y%20%3D%20%5Cbeta_%7B0%7D%20&plus;%20%5Cbeta_%7B1%7DX_%7Bdummy%7D%20&plus;%20%5Cvarepsilon)

ANOVA: ![](http://latex.codecogs.com/svg.latex?Y%20%3D%20%5Cbeta_%7B0%7D%20&plus;%20%5Cbeta_%7B1%7DX_%7B1%20dummy%7D%20&plus;%20%5Cbeta_%7B2%7DX_%7B2%20dummy%7D%20...%20&plus;%20%5Cvarepsilon)

The prototypical regression is conceptualized with X as a continuous variable. However, the only assumption that is actually made about X is that it is a vector of known constants. It could be a continuous variable, but it could also be a dummy code (i.e., a vector of 0's & 1's that indicates whether an observation is a member of an indicated group--e.g., a treatment group). Thus, in the second equation, X could be such a dummy code, and the p-value would be the same as that from a t-test in its more traditional form.

The meaning of the betas would differ here, though. In this case, β0 would be the mean of the control group (for which the entries in the dummy variable would be 0's), and β1 would be the difference between the mean of the treatment group and the mean of the control group.

Now, remember that it is perfectly reasonable to have / run an ANOVA with only two groups (although a t-test would be more common), and you have all three connected. If you prefer seeing how it would work if you had an ANOVA with 3 groups; it would be:

Note that when you have g groups, you have g−1 dummy codes to represent them. The reference group (typically the control group) is indicated by having 0's for all dummy codes (in this case, both dummy code 1 & dummy code 2). In this case, you would not want to interpret the p-values of the t-tests for these betas that come with standard statistical output--they only indicate whether the indicated group differs from the control group when assessed in isolation. That is, these tests are not independent. Instead, you would want to assess whether the group means vary by constructing an ANOVA table and conducting an F-test. For what it's worth, the betas are interpreted just as with the t-test version described above: β0 is the mean of the control / reference group, β1 indicates the difference between the means of group 1 and the reference group, and β2 indicates the difference between group 2 and the reference group.

