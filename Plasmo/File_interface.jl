# using JLD2
# close(f)
# f = jldopen("example3.jld2", "a+")
jldopen("example4.jld2", "w") do file
    file["bigdata"] = randn(5)
end

using FileIO
load("example4.jld2")
