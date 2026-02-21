#ifndef APPSTATE_H
#define APPSTATE_H

#include <vector>
#include <imgui.h>
#include "neurons/neurons.h"
#include "samples.h"

struct ClassifierData
{
    neurons::TypeClassifier type_preceptron;
    std::vector<ClSample> train;
    std::vector<ClSample> test;
    std::vector<ClWeights> history;
    ClWeights current_weights{0, 1, 0};
};

struct RegressionData
{
    std::vector<RegSample> train;
    std::vector<RegSample> test;
    std::vector<RegWeights> history;
    RegWeights current_weights{0, 0};
};

struct AppState
{
    ClassifierData class_data;
    RegressionData reg_data;

    int iteration = 0;

    bool isPlaying = false;
    float playSpeed = 1.0f;
    double lastUpdateTime = 0.0;

    ImVec2 offset = ImVec2(0.0f, 0.0f);
    double scale = 44.0;
    bool isDragging = false;
    ImVec2 dragStart;

    enum CurrentShownData {
        Regression,
        ClassificationThreshold,
        ClassificationBias,
    };
    CurrentShownData currentShownData = Regression;
};

#endif //APPSTATE_H