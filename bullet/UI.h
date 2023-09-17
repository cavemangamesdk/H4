#include <cstdint>
#include <string>
#include <functional>

#include <raylib.h>

constexpr int32_t textPadding = 8;

constexpr float padding = 4.0f;
constexpr float topbarHeight = 38.0f;
constexpr float buttonHeight = topbarHeight - (padding * 2.0f);

static char buffer[256] = { 0 };

struct TopPanelButton {
    std::string Label;
    std::function<void()> Callback;
};

inline void DrawTopPanel(float windowWidth, float height, const std::vector<TopPanelButton>& buttons)
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

inline void DrawStartGamePanel(Vector2 windowSize, Vector2 panelSize)
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

inline void DrawAboutPanel(Vector2 windowSize, Vector2 panelSize, bool* showAboutPanel)
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
