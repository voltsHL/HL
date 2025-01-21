-- Create the main UI
local Infernium = Instance.new("ScreenGui")
local MainFrame = Instance.new("Frame")
local Sidebar = Instance.new("Frame")

-- Sections List
local sections = {"Player", "Legit", "Rage", "Parry", "ESP", "Sounds", "Changer", "World", "Misc"}

-- Setup UI
Infernium.Parent = game.Players.LocalPlayer:WaitForChild("PlayerGui")

MainFrame.Parent = Infernium
MainFrame.Size = UDim2.new(0, 400, 0, 300)
MainFrame.Position = UDim2.new(0.5, -200, 0.5, -150)
MainFrame.BackgroundColor3 = Color3.fromRGB(46, 26, 71) -- Dark purple theme

Sidebar.Parent = MainFrame
Sidebar.Size = UDim2.new(0, 100, 1, 0)
Sidebar.BackgroundColor3 = Color3.fromRGB(31, 18, 48)

-- Add Sidebar Buttons
for _, section in ipairs(sections) do
    local Button = Instance.new("TextButton")
    Button.Parent = Sidebar
    Button.Size = UDim2.new(1, 0, 0, 30)
    Button.Text = section
    Button.BackgroundColor3 = Color3.fromRGB(59, 36, 95)
    Button.TextColor3 = Color3.fromRGB(255, 255, 255)
end

-- Sliders and Toggles
local function createSlider(name, min, max, default, callback)
    local Slider = Instance.new("TextLabel")
    Slider.Parent = MainFrame
    Slider.Text = name .. ": " .. tostring(default)
    Slider.Position = UDim2.new(0.3, 0, 0.1 * #MainFrame:GetChildren(), 0)
    Slider.Size = UDim2.new(0, 150, 0, 30)
    Slider.BackgroundColor3 = Color3.fromRGB(80, 50, 120)
    Slider.TextColor3 = Color3.fromRGB(255, 255, 255)

    local SliderBar = Instance.new("TextButton")
    SliderBar.Parent = Slider
    SliderBar.Size = UDim2.new(0, 100, 0, 10)
    SliderBar.Position = UDim2.new(0.1, 0, 1, 0)
    SliderBar.BackgroundColor3 = Color3.fromRGB(150, 100, 200)

    SliderBar.MouseButton1Click:Connect(function()
        local newValue = math.random(min, max)
        Slider.Text = name .. ": " .. tostring(newValue)
        callback(newValue)
    end)
end

local function createToggle(name, callback)
    local Toggle = Instance.new("TextButton")
    Toggle.Parent = MainFrame
    Toggle.Text = name .. ": OFF"
    Toggle.Size = UDim2.new(0, 150, 0, 30)
    Toggle.Position = UDim2.new(0.3, 0, 0.1 * #MainFrame:GetChildren(), 0)
    Toggle.BackgroundColor3 = Color3.fromRGB(80, 50, 120)
    Toggle.TextColor3 = Color3.fromRGB(255, 255, 255)

    local state = false
    Toggle.MouseButton1Click:Connect(function()
        state = not state
        Toggle.Text = name .. ": " .. (state and "ON" or "OFF")
        callback(state)
    end)
end

-- Adding Sliders
createSlider("Walk Speed", 10, 100, 40, function(value)
    game.Players.LocalPlayer.Character.Humanoid.WalkSpeed = value
end)

createToggle("Fly Toggle", function(state)
    if state then
        game.Players.LocalPlayer.Character.HumanoidRootPart.Anchored = true
    else
        game.Players.LocalPlayer.Character.HumanoidRootPart.Anchored = false
    end
end)

createSlider("Fly Speed", 10, 100, 50, function(value)
    -- Fake fly speed, since flying requires a full fly script
    print("Fly Speed set to", value)
end)

createToggle("FOV Toggle", function(state)
    if state then
        game.Workspace.CurrentCamera.FieldOfView = 120
    else
        game.Workspace.CurrentCamera.FieldOfView = 70
    end
end)

createSlider("FOV", 30, 120, 70, function(value)
    game.Workspace.CurrentCamera.FieldOfView = value
end)

-- Load UI
Infernium.Parent = game.CoreGui
