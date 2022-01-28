| Y          | X          | investigate | # data groups | distribution | test                           |
|------------|------------|-------------|---------------|--------------|--------------------------------|
| discrete   | discrete   |             |               |              | chi square test                |
|            | continuous |             |               |              | logistic regression            |
| continuous | discrete   | mean        | 1             | normal       | 1 sample t-test                |
|            |            |             |               |              | paired t-test                  |
|            |            |             |               | non-normal   | 1 sample Wilcoxon test         |
|            |            |             | 2             | normal       | 2 sample t-test                |
|            |            |             |               | non-normal   | Mann-Whitney test              |
|            |            |             | >2            | normal       | 1 way Anova                    |
|            |            |             |               | non-normal   | Kruskal-Wallis test            |
|            |            | variance    | 2             | normal       | F-test                         |
|            |            |             |               | non-normal   | Levene’s test                  |
|            |            |             | >2            | normal       | Bartlett’s test                |
|            |            |             |               | non-normal   | Levene’s test                  |
|            | continuous |             |               |              | regression                     |