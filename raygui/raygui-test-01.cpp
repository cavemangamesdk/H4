#include <cstdint>
#include <cstdio>
#include <raylib.h>
#define RAYGUI_IMPLEMENTATION
#include "raygui.h"

#include <functional>
#include <vector>
#include <string>

#define WINDOW_WIDTH 1366
#define WINDOW_HEIGHT 768

constexpr int32_t textPadding = 8;

constexpr float padding = 4.0f;
constexpr float topbarHeight = 38.0f;
constexpr float buttonHeight = topbarHeight - (padding * 2.0f);

static char buffer[256] = { 0 };

struct TopPanelButton {
    std::string Label;
    std::function<void()> Callback;
};

void DrawTopPanel(float windowWidth, float height, const std::vector<TopPanelButton>& buttons);
void DrawStartGamePanel(Vector2 windowSize, Vector2 panelSize);
void DrawAboutPanel(Vector2 windowSize, Vector2 panelSize, bool* showAboutPanel);

int main() {
    printf("Hello, raylib (+ raygui)!\n");

    InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, "raylib [core] example - basic window");
    SetWindowState(FLAG_WINDOW_RESIZABLE);

    // constexpr const char* str = "Congrats! You created your first window!";
    // constexpr float fontSize = 20.0f;
    // Vector2 textSize = MeasureTextEx(GetFontDefault(), str,fontSize, 1.0f);

    int32_t windowWidth = WINDOW_WIDTH;
    int32_t windowHeight = WINDOW_HEIGHT;

    constexpr float startGamePanelWidth = 1024.0f;
    constexpr float startGamePanelHeight = 512.0f;

    bool showAboutPanel = false;

    std::vector<TopPanelButton> topPanelButtons = {
        (TopPanelButton){
            GuiIconText(ICON_FILE_SAVE, "Save CSV"),
            [&]() {}
        },
        (TopPanelButton){
           GuiIconText(ICON_FILE_OPEN, "Open CSV"),
            [&]() {}
        }, 
        (TopPanelButton){
            "About",
            [&]() { showAboutPanel = !showAboutPanel; }
        }
    };

    while (!WindowShouldClose()) {
        if(IsWindowResized()) {
            windowWidth = GetRenderWidth();
            windowHeight = GetRenderHeight();
            printf("%d, %d\n", windowWidth, windowHeight);
        }

        BeginDrawing();
        ClearBackground(RAYWHITE);

        DrawTopPanel((float)windowWidth, topbarHeight, topPanelButtons);

        DrawStartGamePanel({(float)windowWidth, (float)windowHeight}, {startGamePanelWidth, startGamePanelHeight});

        if(showAboutPanel) {
            DrawAboutPanel({(float)windowWidth, (float)windowHeight}, {512, 256}, &showAboutPanel);
        }

        // GuiListView((Rectangle){ 165, 25, 140, 124 }, "Charmander;Bulbasaur;#18#Squirtel;Pikachu;Eevee;Pidgey", &listViewScrollIndex, &listViewActive);
        // int32_t x = (int32_t)((float)windowWidth / 2.0f) - (textSize.x / 2.0f); 
        // int32_t y = (int32_t)((float)windowHeight / 2.0f) - (textSize.y / 2.0f);
        // DrawText("Congrats! You created your first window!", x, y, fontSize, BLACK);

        EndDrawing();
    }

    CloseWindow();

    return 0;
}

constexpr float buttonWidth = 90.0f;

void DrawTopPanel(float windowWidth, float height, const std::vector<TopPanelButton>& buttons)
{
    float xPosition = padding;

    GuiDrawRectangle({0, 0, (float)windowWidth, height}, 0, BLACK, LIGHTGRAY);

    int buttonTextPadding = GuiGetStyle(BUTTON, TEXT_PADDING);
    GuiSetStyle(BUTTON, TEXT_PADDING, textPadding);

    for(size_t i = 0; i < buttons.size(); i++) {
        if(GuiButton({xPosition, padding, buttonWidth, buttonHeight }, buttons[i].Label.c_str())) {
            buttons[i].Callback();
        }
        xPosition += buttonWidth + padding;
    }

    GuiSetStyle(BUTTON, TEXT_PADDING, buttonTextPadding);
}

void DrawStartGamePanel(Vector2 windowSize, Vector2 panelSize)
{
    int result = GuiTextInputBox((Rectangle){ (float)GetScreenWidth()/2 - 120, (float)GetScreenHeight()/2 - 60, 240, 140 }, GuiIconText(ICON_FILE_SAVE, "Enter player name:"), "Enter player name:", "Start;Quit", buffer, 255, NULL);

    if (result == 1)
    {
        // TODO: Validate textInput value and save
        if ((buffer != NULL) && (buffer[0] == '\0')) {
            printf("Player name is empty\n");
            return;
        }

        printf("%s\n", buffer);

        // TODO: Change game state
    }

    if ((result == 0) || (result == 1) || (result == 2))
    {
        TextCopy(buffer, "\0");
        if((result == 0) || (result == 2))
        {
            exit(0);
        }
    }
}

void DrawAboutPanel(Vector2 windowSize, Vector2 panelSize, bool* showAboutPanel)
{
    float x = (windowSize.x / 2.0f) - (panelSize.x / 2.0f);
    float y = (windowSize.y / 2.0f) - (panelSize.y / 2.0f);
    int32_t windowBox = GuiWindowBox({x, y, panelSize.x, panelSize.y}, "About");
    if(windowBox == 1) { // Close button pressed
        *showAboutPanel = false;
    }

    constexpr const char* madeByText = "Made by Michael, Victor & Pierre";
    constexpr float fontSize = 24.0f;
    constexpr float spacing = 1.0f;

    Vector2 textSize = MeasureTextEx(GetFontDefault(), madeByText, fontSize, spacing);

    x = (windowSize.x / 2.0f) - (textSize.x / 2.0f);
    y = (windowSize.y / 2.0f) - (textSize.y / 2.0f);
    DrawText(madeByText, x, y, (int32_t)fontSize, BLACK);
}
