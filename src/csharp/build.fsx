// include Fake lib
#r "packages/FAKE/tools/FakeLib.dll"
open Fake

// Properties

Target "BuildApp" (fun _ ->
    !! "CodeWarsKatas.sln"
    |> MSBuildRelease null "Build"
    |> ignore
)

// Dependencies
"BuildApp"

// start build
RunTargetOrDefault "BuildApp"