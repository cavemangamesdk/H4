#include "raylib.h"
#include "raymath.h"

int main() {
    const int screenWidth = 800;
    const int screenHeight = 450;

    InitWindow(screenWidth, screenHeight, "Rotate 3D Cube");

    Camera3D camera = { 0 };
    camera.position = (Vector3){ 0.0f, 10.0f, 10.0f };
    camera.target = (Vector3){ 0.0f, 0.0f, 0.0f };
    camera.up = (Vector3){ 0.0f, 1.0f, 0.0f };
    camera.fovy = 45.0f;
    camera.projection = CAMERA_PERSPECTIVE;

    Model model = LoadModel("resources/models/cube.obj");
    Texture2D texture = LoadTexture("resources/models/cube_diffuse.png");
    model.materials[0].maps[MATERIAL_MAP_DIFFUSE].texture = texture;

    Vector3 rotationAxis = { 0.0f, 1.0f, 0.0f };
    float rotationAngle = 0.0f;

    SetTargetFPS(60);

    while (!WindowShouldClose()) {
        rotationAngle += 1.0f;

        if (rotationAngle >= 360.0f) {
            rotationAngle -= 360.0f;
        }

        Matrix rotationMatrix = MatrixRotate(rotationAxis, rotationAngle * DEG2RAD);

        BeginDrawing();
        ClearBackground(RAYWHITE);

        BeginMode3D(camera);

        UpdateCamera(&camera, CAMERA_FREE);

        model.transform = MatrixMultiply(model.transform, rotationMatrix);

        DrawModel(model, Vector3Zero(), 1.0f, WHITE);

        EndMode3D();

        EndDrawing();
    }

    UnloadModel(model);
    UnloadTexture(texture);

    CloseWindow();

    return 0;
}
