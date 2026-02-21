#ifndef WEIGHTS_H
#define WEIGHTS_H

struct ClWeights
{
    double w1;
    double w2;
    double w0;
};

struct RegWeights
{
    double w1 = 0.0;
    double w0 = 0.5;
};

#endif //WEIGHTS_H