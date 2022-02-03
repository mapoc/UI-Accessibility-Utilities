import numpy as np
from mashop.microtoolkit.toolkit import APIError, status_codes
from mashop.utilities import build_uv_svr_error_response


RGB = np.array([ \
 [0,0,0] \
,[0,0,128] \
,[0,0,139] \
,[0,0,139] \
,[0,0,205] \
,[0,0,205] \
,[0,0,238] \
,[0,0,255] \
,[0,0,255] \
,[0,100,0] \
,[0,104,139] \
,[0,128,0] \
,[0,128,0] \
,[0,128,128] \
,[0,134,139] \
,[0,139,0] \
,[0,139,69] \
,[0,139,139] \
,[0,139,139] \
,[0,154,205] \
,[0,178,238] \
,[0,191,255] \
,[0,191,255] \
,[0,197,205] \
,[0,205,0] \
,[0,205,102] \
,[0,205,205] \
,[0,206,209] \
,[0,229,238] \
,[0,238,0] \
,[0,238,118] \
,[0,238,238] \
,[0,245,255] \
,[0,250,154] \
,[0,255,0] \
,[0,255,0] \
,[0,255,0] \
,[0,255,0] \
,[0,255,127] \
,[0,255,127] \
,[0,255,255] \
,[0,255,255] \
,[0,255,255] \
,[2,102,102] \
,[3,3,3] \
,[5,5,5] \
,[8,8,8] \
,[10,10,10] \
,[13,13,13] \
,[15,15,15] \
,[16,78,139] \
,[18,18,18] \
,[20,20,20] \
,[23,23,23] \
,[24,116,205] \
,[25,25,112] \
,[26,26,26] \
,[28,28,28] \
,[28,134,238] \
,[30,144,255] \
,[30,144,255] \
,[31,31,31] \
,[32,178,170] \
,[33,33,33] \
,[34,139,34] \
,[36,36,36] \
,[38,38,38] \
,[39,64,139] \
,[41,41,41] \
,[43,43,43] \
,[46,46,46] \
,[46,139,87] \
,[46,139,87] \
,[47,79,79] \
,[48,48,48] \
,[50,205,50] \
,[51,51,51] \
,[54,54,54] \
,[54,100,139] \
,[56,56,56] \
,[58,95,205] \
,[59,59,59] \
,[60,179,113] \
,[61,61,61] \
,[64,64,64] \
,[64,224,208] \
,[65,105,225] \
,[66,66,66] \
,[67,110,238] \
,[67,205,128] \
,[69,69,69] \
,[69,139,0] \
,[69,139,116] \
,[70,130,180] \
,[71,60,139] \
,[71,71,71] \
,[72,61,139] \
,[72,118,255] \
,[72,209,204] \
,[74,74,74] \
,[74,112,139] \
,[75,0,130] \
,[77,77,77] \
,[78,238,148] \
,[79,79,79] \
,[79,148,205] \
,[82,82,82] \
,[82,139,139] \
,[83,134,139] \
,[84,84,84] \
,[84,139,84] \
,[84,255,159] \
,[85,26,139] \
,[85,107,47] \
,[87,87,87] \
,[89,89,89] \
,[92,92,92] \
,[92,172,238] \
,[93,71,139] \
,[94,94,94] \
,[95,158,160] \
,[96,123,139] \
,[97,97,97] \
,[99,99,99] \
,[99,184,255] \
,[100,149,237] \
,[102,51,153] \
,[102,139,139] \
,[102,205,0] \
,[102,205,170] \
,[102,205,170] \
,[104,34,139] \
,[104,131,139] \
,[105,89,205] \
,[105,105,105] \
,[105,105,105] \
,[105,139,34] \
,[105,139,105] \
,[106,90,205] \
,[107,107,107] \
,[107,142,35] \
,[108,123,139] \
,[108,166,205] \
,[110,110,110] \
,[110,123,139] \
,[110,139,61] \
,[112,112,112] \
,[112,128,144] \
,[115,115,115] \
,[117,117,117] \
,[118,238,0] \
,[118,238,198] \
,[119,136,153] \
,[120,120,120] \
,[121,205,205] \
,[122,55,139] \
,[122,103,238] \
,[122,122,122] \
,[122,139,139] \
,[122,197,205] \
,[123,104,238] \
,[124,205,124] \
,[124,252,0] \
,[125,38,205] \
,[125,125,125] \
,[126,192,238] \
,[127,127,127] \
,[127,255,0] \
,[127,255,0] \
,[127,255,212] \
,[127,255,212] \
,[128,0,0] \
,[128,0,0] \
,[128,0,128] \
,[128,0,128] \
,[128,128,0] \
,[128,128,128] \
,[128,128,128] \
,[130,130,130] \
,[131,111,255] \
,[131,139,131] \
,[131,139,139] \
,[132,112,255] \
,[133,133,133] \
,[135,135,135] \
,[135,206,235] \
,[135,206,250] \
,[135,206,255] \
,[137,104,205] \
,[138,43,226] \
,[138,138,138] \
,[139,0,0] \
,[139,0,0] \
,[139,0,139] \
,[139,0,139] \
,[139,10,80] \
,[139,26,26] \
,[139,28,98] \
,[139,34,82] \
,[139,35,35] \
,[139,37,0] \
,[139,54,38] \
,[139,58,58] \
,[139,58,98] \
,[139,62,47] \
,[139,69,0] \
,[139,69,19] \
,[139,69,19] \
,[139,71,38] \
,[139,71,93] \
,[139,71,137] \
,[139,76,57] \
,[139,87,66] \
,[139,90,0] \
,[139,90,43] \
,[139,95,101] \
,[139,99,108] \
,[139,101,8] \
,[139,102,139] \
,[139,105,20] \
,[139,105,105] \
,[139,115,85] \
,[139,117,0] \
,[139,119,101] \
,[139,121,94] \
,[139,123,139] \
,[139,125,107] \
,[139,125,123] \
,[139,126,102] \
,[139,129,76] \
,[139,131,120] \
,[139,131,134] \
,[139,134,78] \
,[139,134,130] \
,[139,136,120] \
,[139,137,112] \
,[139,137,137] \
,[139,139,0] \
,[139,139,122] \
,[139,139,131] \
,[140,140,140] \
,[141,182,205] \
,[141,238,238] \
,[142,229,238] \
,[143,143,143] \
,[143,188,143] \
,[144,238,144] \
,[144,238,144] \
,[145,44,238] \
,[145,145,145] \
,[147,112,219] \
,[148,0,211] \
,[148,148,148] \
,[150,150,150] \
,[150,205,205] \
,[151,255,255] \
,[152,245,255] \
,[152,251,152] \
,[153,50,204] \
,[153,153,153] \
,[154,50,205] \
,[154,192,205] \
,[154,205,50] \
,[154,205,50] \
,[154,255,154] \
,[155,48,255] \
,[155,205,155] \
,[156,156,156] \
,[158,158,158] \
,[159,121,238] \
,[159,182,205] \
,[160,32,240] \
,[160,32,240] \
,[160,82,45] \
,[161,161,161] \
,[162,181,205] \
,[162,205,90] \
,[163,163,163] \
,[164,211,238] \
,[165,42,42] \
,[166,166,166] \
,[168,168,168] \
,[169,169,169] \
,[171,130,255] \
,[171,171,171] \
,[173,173,173] \
,[173,216,230] \
,[173,255,47] \
,[174,238,238] \
,[175,238,238] \
,[176,48,96] \
,[176,48,96] \
,[176,176,176] \
,[176,196,222] \
,[176,224,230] \
,[176,226,255] \
,[178,34,34] \
,[178,58,238] \
,[178,223,238] \
,[179,179,179] \
,[179,238,58] \
,[180,82,205] \
,[180,205,205] \
,[180,238,180] \
,[181,181,181] \
,[184,134,11] \
,[184,184,184] \
,[185,211,238] \
,[186,85,211] \
,[186,186,186] \
,[187,255,255] \
,[188,143,143] \
,[188,210,238] \
,[188,238,104] \
,[189,183,107] \
,[189,189,189] \
,[190,190,190] \
,[190,190,190] \
,[191,62,255] \
,[191,191,191] \
,[191,239,255] \
,[192,192,192] \
,[192,255,62] \
,[193,205,193] \
,[193,205,205] \
,[193,255,193] \
,[194,194,194] \
,[196,196,196] \
,[198,226,255] \
,[199,21,133] \
,[199,199,199] \
,[201,201,201] \
,[202,225,255] \
,[202,255,112] \
,[204,204,204] \
,[205,0,0] \
,[205,0,205] \
,[205,16,118] \
,[205,38,38] \
,[205,41,144] \
,[205,50,120] \
,[205,51,51] \
,[205,55,0] \
,[205,79,57] \
,[205,85,85] \
,[205,91,69] \
,[205,92,92] \
,[205,96,144] \
,[205,102,0] \
,[205,102,29] \
,[205,104,57] \
,[205,104,137] \
,[205,105,201] \
,[205,112,84] \
,[205,129,98] \
,[205,133,0] \
,[205,133,63] \
,[205,133,63] \
,[205,140,149] \
,[205,145,158] \
,[205,149,12] \
,[205,150,205] \
,[205,155,29] \
,[205,155,155] \
,[205,170,125] \
,[205,173,0] \
,[205,175,149] \
,[205,179,139] \
,[205,181,205] \
,[205,183,158] \
,[205,183,181] \
,[205,186,150] \
,[205,190,112] \
,[205,192,176] \
,[205,193,197] \
,[205,197,191] \
,[205,198,115] \
,[205,200,177] \
,[205,201,165] \
,[205,201,201] \
,[205,205,0] \
,[205,205,180] \
,[205,205,193] \
,[207,207,207] \
,[208,32,144] \
,[209,95,238] \
,[209,209,209] \
,[209,238,238] \
,[210,105,30] \
,[210,180,140] \
,[211,211,211] \
,[212,212,212] \
,[214,214,214] \
,[216,191,216] \
,[217,217,217] \
,[218,112,214] \
,[218,165,32] \
,[219,112,147] \
,[219,219,219] \
,[220,20,60] \
,[220,220,220] \
,[221,160,221] \
,[222,184,135] \
,[222,222,222] \
,[224,102,255] \
,[224,224,224] \
,[224,238,224] \
,[224,238,238] \
,[224,255,255] \
,[224,255,255] \
,[227,227,227] \
,[229,229,229] \
,[230,230,250] \
,[232,232,232] \
,[233,150,122] \
,[235,235,235] \
,[237,237,237] \
,[238,0,0] \
,[238,0,238] \
,[238,18,137] \
,[238,44,44] \
,[238,48,167] \
,[238,58,140] \
,[238,59,59] \
,[238,64,0] \
,[238,92,66] \
,[238,99,99] \
,[238,106,80] \
,[238,106,167] \
,[238,118,0] \
,[238,118,33] \
,[238,121,66] \
,[238,121,159] \
,[238,122,233] \
,[238,130,98] \
,[238,130,238] \
,[238,149,114] \
,[238,154,0] \
,[238,154,73] \
,[238,162,173] \
,[238,169,184] \
,[238,173,14] \
,[238,174,238] \
,[238,180,34] \
,[238,180,180] \
,[238,197,145] \
,[238,201,0] \
,[238,203,173] \
,[238,207,161] \
,[238,210,238] \
,[238,213,183] \
,[238,213,210] \
,[238,216,174] \
,[238,220,130] \
,[238,221,130] \
,[238,223,204] \
,[238,224,229] \
,[238,229,222] \
,[238,230,133] \
,[238,232,170] \
,[238,232,205] \
,[238,233,191] \
,[238,233,233] \
,[238,238,0] \
,[238,238,209] \
,[238,238,224] \
,[240,128,128] \
,[240,230,140] \
,[240,240,240] \
,[240,248,255] \
,[240,255,240] \
,[240,255,240] \
,[240,255,255] \
,[240,255,255] \
,[242,242,242] \
,[244,164,96] \
,[245,222,179] \
,[245,245,220] \
,[245,245,245] \
,[245,245,245] \
,[245,255,250] \
,[247,247,247] \
,[248,248,255] \
,[250,128,114] \
,[250,235,215] \
,[250,240,230] \
,[250,250,210] \
,[250,250,250] \
,[252,252,252] \
,[253,245,230] \
,[255,0,0] \
,[255,0,0] \
,[255,0,255] \
,[255,0,255] \
,[255,0,255] \
,[255,20,147] \
,[255,20,147] \
,[255,48,48] \
,[255,52,179] \
,[255,62,150] \
,[255,64,64] \
,[255,69,0] \
,[255,69,0] \
,[255,99,71] \
,[255,99,71] \
,[255,105,180] \
,[255,106,106] \
,[255,110,180] \
,[255,114,86] \
,[255,127,0] \
,[255,127,36] \
,[255,127,80] \
,[255,130,71] \
,[255,130,171] \
,[255,131,250] \
,[255,140,0] \
,[255,140,105] \
,[255,160,122] \
,[255,160,122] \
,[255,165,0] \
,[255,165,0] \
,[255,165,79] \
,[255,174,185] \
,[255,181,197] \
,[255,182,193] \
,[255,185,15] \
,[255,187,255] \
,[255,192,203] \
,[255,193,37] \
,[255,193,193] \
,[255,211,155] \
,[255,215,0] \
,[255,215,0] \
,[255,218,185] \
,[255,218,185] \
,[255,222,173] \
,[255,222,173] \
,[255,225,255] \
,[255,228,181] \
,[255,228,196] \
,[255,228,196] \
,[255,228,225] \
,[255,228,225] \
,[255,231,186] \
,[255,235,205] \
,[255,236,139] \
,[255,239,213] \
,[255,239,219] \
,[255,240,245] \
,[255,240,245] \
,[255,245,238] \
,[255,245,238] \
,[255,246,143] \
,[255,248,220] \
,[255,248,220] \
,[255,250,205] \
,[255,250,205] \
,[255,250,240] \
,[255,250,250] \
,[255,250,250] \
,[255,255,0] \
,[255,255,0] \
,[255,255,224] \
,[255,255,224] \
,[255,255,240] \
,[255,255,240] \
,[255,255,255] \
,[255,255,255] \
])
HEX_NAME_DICT = { \
 "#000000":"black" \
,"#000000":"gray0" \
,"#000080":"navy" \
,"#000080":"NavyBlue" \
,"#00008B":"blue4" \
,"#00008B":"DarkBlue" \
,"#0000CD":"MediumBlue" \
,"#0000CD":"blue3" \
,"#0000EE":"blue2" \
,"#0000FF":"blue" \
,"#0000FF":"blue1" \
,"#006400":"DarkGreen" \
,"#00688B":"DeepSkyBlue4" \
,"#008000":"WebGreen" \
,"#008000":"green" \
,"#008080":"teal" \
,"#00868B":"turquoise4" \
,"#008B00":"green4" \
,"#008B45":"SpringGreen4" \
,"#008B8B":"cyan4" \
,"#008B8B":"DarkCyan" \
,"#009ACD":"DeepSkyBlue3" \
,"#00B2EE":"DeepSkyBlue2" \
,"#00BFFF":"DeepSkyBlue" \
,"#00BFFF":"DeepSkyBlue1" \
,"#00C5CD":"turquoise3" \
,"#00CD00":"green3" \
,"#00CD66":"SpringGreen3" \
,"#00CDCD":"cyan3" \
,"#00CED1":"DarkTurquoise" \
,"#00E5EE":"turquoise2" \
,"#00EE00":"green2" \
,"#00EE76":"SpringGreen2" \
,"#00EEEE":"cyan2" \
,"#00F5FF":"turquoise1" \
,"#00FA9A":"MediumSpringGreen" \
,"#00FF00":"lime" \
,"#00FF00":"green" \
,"#00FF00":"green1" \
,"#00FF00":"X11Green" \
,"#00FF7F":"SpringGreen" \
,"#00FF7F":"SpringGreen1" \
,"#00FFFF":"cyan1" \
,"#00FFFF":"aqua" \
,"#00FFFF":"cyan" \
,"#026666":"gray40" \
,"#030303":"gray1" \
,"#050505":"gray2" \
,"#080808":"gray3" \
,"#0A0A0A":"gray4" \
,"#0D0D0D":"gray5" \
,"#0F0F0F":"gray6" \
,"#104E8B":"DodgerBlue4" \
,"#121212":"gray7" \
,"#141414":"gray8" \
,"#171717":"gray9" \
,"#1874CD":"DodgerBlue3" \
,"#191970":"MidnightBlue" \
,"#1A1A1A":"gray10" \
,"#1C1C1C":"gray11" \
,"#1C86EE":"DodgerBlue2" \
,"#1E90FF":"DodgerBlue" \
,"#1E90FF":"DodgerBlue1" \
,"#1F1F1F":"gray12" \
,"#20B2AA":"LightSeaGreen" \
,"#212121":"gray13" \
,"#228B22":"ForestGreen" \
,"#242424":"gray14" \
,"#262626":"gray15" \
,"#27408B":"RoyalBlue4" \
,"#292929":"gray16" \
,"#2B2B2B":"gray17" \
,"#2E2E2E":"gray18" \
,"#2E8B57":"SeaGreen" \
,"#2E8B57":"SeaGreen4" \
,"#2F4F4F":"DarkSlateGray" \
,"#303030":"gray19" \
,"#32CD32":"LimeGreen" \
,"#333333":"gray20" \
,"#363636":"gray21" \
,"#36648B":"SteelBlue4" \
,"#383838":"gray22" \
,"#3A5FCD":"RoyalBlue3" \
,"#3B3B3B":"gray23" \
,"#3CB371":"MediumSeaGreen" \
,"#3D3D3D":"gray24" \
,"#404040":"gray25" \
,"#40E0D0":"turquoise" \
,"#4169E1":"RoyalBlue" \
,"#424242":"gray26" \
,"#436EEE":"RoyalBlue2" \
,"#43CD80":"SeaGreen3" \
,"#454545":"gray27" \
,"#458B00":"chartreuse4" \
,"#458B74":"aquamarine4" \
,"#4682B4":"SteelBlue" \
,"#473C8B":"SlateBlue4" \
,"#474747":"gray28" \
,"#483D8B":"DarkSlateBlue" \
,"#4876FF":"RoyalBlue1" \
,"#48D1CC":"MediumTurquoise" \
,"#4A4A4A":"gray29" \
,"#4A708B":"SkyBlue4" \
,"#4B0082":"indigo" \
,"#4D4D4D":"gray30" \
,"#4EEE94":"SeaGreen2" \
,"#4F4F4F":"gray31" \
,"#4F94CD":"SteelBlue3" \
,"#525252":"gray32" \
,"#528B8B":"DarkSlateGray4" \
,"#53868B":"CadetBlue4" \
,"#545454":"gray33" \
,"#548B54":"PaleGreen4" \
,"#54FF9F":"SeaGreen1" \
,"#551A8B":"purple4" \
,"#556B2F":"DarkOliveGreen" \
,"#575757":"gray34" \
,"#595959":"gray35" \
,"#5C5C5C":"gray36" \
,"#5CACEE":"SteelBlue2" \
,"#5D478B":"MediumPurple4" \
,"#5E5E5E":"gray37" \
,"#5F9EA0":"CadetBlue" \
,"#607B8B":"LightSkyBlue4" \
,"#616161":"gray38" \
,"#636363":"gray39" \
,"#63B8FF":"SteelBlue1" \
,"#6495ED":"CornflowerBlue" \
,"#663399":"RebeccaPurple" \
,"#668B8B":"PaleTurquoise4" \
,"#66CD00":"chartreuse3" \
,"#66CDAA":"MediumAquamarine" \
,"#66CDAA":"aquamarine3" \
,"#68228B":"DarkOrchid4" \
,"#68838B":"LightBlue4" \
,"#6959CD":"SlateBlue3" \
,"#696969":"DimGray" \
,"#696969":"gray41" \
,"#698B22":"OliveDrab4" \
,"#698B69":"DarkSeaGreen4" \
,"#6A5ACD":"SlateBlue" \
,"#6B6B6B":"gray42" \
,"#6B8E23":"OliveDrab" \
,"#6C7B8B":"SlateGray4" \
,"#6CA6CD":"SkyBlue3" \
,"#6E6E6E":"gray43" \
,"#6E7B8B":"LightSteelBlue4" \
,"#6E8B3D":"DarkOliveGreen4" \
,"#707070":"gray44" \
,"#708090":"SlateGray" \
,"#737373":"gray45" \
,"#757575":"gray46" \
,"#76EE00":"chartreuse2" \
,"#76EEC6":"aquamarine2" \
,"#778899":"LightSlateGray" \
,"#787878":"gray47" \
,"#79CDCD":"DarkSlateGray3" \
,"#7A378B":"MediumOrchid4" \
,"#7A67EE":"SlateBlue2" \
,"#7A7A7A":"gray48" \
,"#7A8B8B":"LightCyan4" \
,"#7AC5CD":"CadetBlue3" \
,"#7B68EE":"MediumSlateBlue" \
,"#7CCD7C":"PaleGreen3" \
,"#7CFC00":"LawnGreen" \
,"#7D26CD":"purple3" \
,"#7D7D7D":"gray49" \
,"#7EC0EE":"SkyBlue2" \
,"#7F7F7F":"gray50" \
,"#7FFF00":"chartreuse" \
,"#7FFF00":"chartreuse1" \
,"#7FFFD4":"aquamarine" \
,"#7FFFD4":"aquamarine1" \
,"#800000":"WebMaroon" \
,"#800000":"maroon" \
,"#800080":"WebPurple" \
,"#800080":"purple" \
,"#808000":"olive" \
,"#808080":"WebGray" \
,"#808080":"gray" \
,"#828282":"gray51" \
,"#836FFF":"SlateBlue1" \
,"#838B83":"honeydew4" \
,"#838B8B":"azure4" \
,"#8470FF":"LightSlateBlue" \
,"#858585":"gray52" \
,"#878787":"gray53" \
,"#87CEEB":"SkyBlue" \
,"#87CEFA":"LightSkyBlue" \
,"#87CEFF":"SkyBlue1" \
,"#8968CD":"MediumPurple3" \
,"#8A2BE2":"BlueViolet" \
,"#8A8A8A":"gray54" \
,"#8B0000":"DarkRed" \
,"#8B0000":"red4" \
,"#8B008B":"DarkMagenta" \
,"#8B008B":"magenta4" \
,"#8B0A50":"DeepPink4" \
,"#8B1A1A":"firebrick4" \
,"#8B1C62":"maroon4" \
,"#8B2252":"VioletRed4" \
,"#8B2323":"brown4" \
,"#8B2500":"OrangeRed4" \
,"#8B3626":"tomato4" \
,"#8B3A3A":"IndianRed4" \
,"#8B3A62":"HotPink4" \
,"#8B3E2F":"coral4" \
,"#8B4500":"DarkOrange4" \
,"#8B4513":"SaddleBrown" \
,"#8B4513":"chocolate4" \
,"#8B4726":"sienna4" \
,"#8B475D":"PaleVioletRed4" \
,"#8B4789":"orchid4" \
,"#8B4C39":"salmon4" \
,"#8B5742":"LightSalmon4" \
,"#8B5A00":"orange4" \
,"#8B5A2B":"tan4" \
,"#8B5F65":"LightPink4" \
,"#8B636C":"pink4" \
,"#8B6508":"DarkGoldenrod4" \
,"#8B668B":"plum4" \
,"#8B6914":"goldenrod4" \
,"#8B6969":"RosyBrown4" \
,"#8B7355":"burlywood4" \
,"#8B7500":"gold4" \
,"#8B7765":"PeachPuff4" \
,"#8B795E":"NavajoWhite4" \
,"#8B7B8B":"thistle4" \
,"#8B7D6B":"bisque4" \
,"#8B7D7B":"MistyRose4" \
,"#8B7E66":"wheat4" \
,"#8B814C":"LightGoldenrod4" \
,"#8B8378":"AntiqueWhite4" \
,"#8B8386":"LavenderBlush4" \
,"#8B864E":"khaki4" \
,"#8B8682":"seashell4" \
,"#8B8878":"cornsilk4" \
,"#8B8970":"LemonChiffon4" \
,"#8B8989":"snow4" \
,"#8B8B00":"yellow4" \
,"#8B8B7A":"LightYellow4" \
,"#8B8B83":"ivory4" \
,"#8C8C8C":"gray55" \
,"#8DB6CD":"LightSkyBlue3" \
,"#8DEEEE":"DarkSlateGray2" \
,"#8EE5EE":"CadetBlue2" \
,"#8F8F8F":"gray56" \
,"#8FBC8F":"DarkSeaGreen" \
,"#90EE90":"LightGreen" \
,"#90EE90":"PaleGreen2" \
,"#912CEE":"purple2" \
,"#919191":"gray57" \
,"#9370DB":"MediumPurple" \
,"#9400D3":"DarkViolet" \
,"#949494":"gray58" \
,"#969696":"gray59" \
,"#96CDCD":"PaleTurquoise3" \
,"#97FFFF":"DarkSlateGray1" \
,"#98F5FF":"CadetBlue1" \
,"#98FB98":"PaleGreen" \
,"#9932CC":"DarkOrchid" \
,"#999999":"gray60" \
,"#9A32CD":"DarkOrchid3" \
,"#9AC0CD":"LightBlue3" \
,"#9ACD32":"YellowGreen" \
,"#9ACD32":"OliveDrab3" \
,"#9AFF9A":"PaleGreen1" \
,"#9B30FF":"purple1" \
,"#9BCD9B":"DarkSeaGreen3" \
,"#9C9C9C":"gray61" \
,"#9E9E9E":"gray62" \
,"#9F79EE":"MediumPurple2" \
,"#9FB6CD":"SlateGray3" \
,"#A020F0":"purple" \
,"#A020F0":"X11Purple" \
,"#A0522D":"sienna" \
,"#A1A1A1":"gray63" \
,"#A2B5CD":"LightSteelBlue3" \
,"#A2CD5A":"DarkOliveGreen3" \
,"#A3A3A3":"gray64" \
,"#A4D3EE":"LightSkyBlue2" \
,"#A52A2A":"brown" \
,"#A6A6A6":"gray65" \
,"#A8A8A8":"gray66" \
,"#A9A9A9":"DarkGray" \
,"#AB82FF":"MediumPurple1" \
,"#ABABAB":"gray67" \
,"#ADADAD":"gray68" \
,"#ADD8E6":"LightBlue" \
,"#ADFF2F":"GreenYellow" \
,"#AEEEEE":"PaleTurquoise2" \
,"#AFEEEE":"PaleTurquoise" \
,"#B03060":"maroon" \
,"#B03060":"X11Maroon" \
,"#B0B0B0":"gray69" \
,"#B0C4DE":"LightSteelBlue" \
,"#B0E0E6":"PowderBlue" \
,"#B0E2FF":"LightSkyBlue1" \
,"#B22222":"firebrick" \
,"#B23AEE":"DarkOrchid2" \
,"#B2DFEE":"LightBlue2" \
,"#B3B3B3":"gray70" \
,"#B3EE3A":"OliveDrab2" \
,"#B452CD":"MediumOrchid3" \
,"#B4CDCD":"LightCyan3" \
,"#B4EEB4":"DarkSeaGreen2" \
,"#B5B5B5":"gray71" \
,"#B8860B":"DarkGoldenrod" \
,"#B8B8B8":"gray72" \
,"#B9D3EE":"SlateGray2" \
,"#BA55D3":"MediumOrchid" \
,"#BABABA":"gray73" \
,"#BBFFFF":"PaleTurquoise1" \
,"#BC8F8F":"RosyBrown" \
,"#BCD2EE":"LightSteelBlue2" \
,"#BCEE68":"DarkOliveGreen2" \
,"#BDB76B":"DarkKhaki" \
,"#BDBDBD":"gray74" \
,"#BEBEBE":"gray" \
,"#BEBEBE":"X11Gray" \
,"#BF3EFF":"DarkOrchid1" \
,"#BFBFBF":"gray75" \
,"#BFEFFF":"LightBlue1" \
,"#C0C0C0":"silver" \
,"#C0FF3E":"OliveDrab1" \
,"#C1CDC1":"honeydew3" \
,"#C1CDCD":"azure3" \
,"#C1FFC1":"DarkSeaGreen1" \
,"#C2C2C2":"gray76" \
,"#C4C4C4":"gray77" \
,"#C6E2FF":"SlateGray1" \
,"#C71585":"MediumVioletRed" \
,"#C7C7C7":"gray78" \
,"#C9C9C9":"gray79" \
,"#CAE1FF":"LightSteelBlue1" \
,"#CAFF70":"DarkOliveGreen1" \
,"#CCCCCC":"gray80" \
,"#CD0000":"red3" \
,"#CD00CD":"magenta3" \
,"#CD1076":"DeepPink3" \
,"#CD2626":"firebrick3" \
,"#CD2990":"maroon3" \
,"#CD3278":"VioletRed3" \
,"#CD3333":"brown3" \
,"#CD3700":"OrangeRed3" \
,"#CD4F39":"tomato3" \
,"#CD5555":"IndianRed3" \
,"#CD5B45":"coral3" \
,"#CD5C5C":"IndianRed" \
,"#CD6090":"HotPink3" \
,"#CD6600":"DarkOrange3" \
,"#CD661D":"chocolate3" \
,"#CD6839":"sienna3" \
,"#CD6889":"PaleVioletRed3" \
,"#CD69C9":"orchid3" \
,"#CD7054":"salmon3" \
,"#CD8162":"LightSalmon3" \
,"#CD8500":"orange3" \
,"#CD853F":"peru" \
,"#CD853F":"tan3" \
,"#CD8C95":"LightPink3" \
,"#CD919E":"pink3" \
,"#CD950C":"DarkGoldenrod3" \
,"#CD96CD":"plum3" \
,"#CD9B1D":"goldenrod3" \
,"#CD9B9B":"RosyBrown3" \
,"#CDAA7D":"burlywood3" \
,"#CDAD00":"gold3" \
,"#CDAF95":"PeachPuff3" \
,"#CDB38B":"NavajoWhite3" \
,"#CDB5CD":"thistle3" \
,"#CDB79E":"bisque3" \
,"#CDB7B5":"MistyRose3" \
,"#CDBA96":"wheat3" \
,"#CDBE70":"LightGoldenrod3" \
,"#CDC0B0":"AntiqueWhite3" \
,"#CDC1C5":"LavenderBlush3" \
,"#CDC5BF":"seashell3" \
,"#CDC673":"khaki3" \
,"#CDC8B1":"cornsilk3" \
,"#CDC9A5":"LemonChiffon3" \
,"#CDC9C9":"snow3" \
,"#CDCD00":"yellow3" \
,"#CDCDB4":"LightYellow3" \
,"#CDCDC1":"ivory3" \
,"#CFCFCF":"gray81" \
,"#D02090":"VioletRed" \
,"#D15FEE":"MediumOrchid2" \
,"#D1D1D1":"gray82" \
,"#D1EEEE":"LightCyan2" \
,"#D2691E":"chocolate" \
,"#D2B48C":"tan" \
,"#D3D3D3":"LightGray" \
,"#D4D4D4":"gray83" \
,"#D6D6D6":"gray84" \
,"#D8BFD8":"thistle" \
,"#D9D9D9":"gray85" \
,"#DA70D6":"orchid" \
,"#DAA520":"goldenrod" \
,"#DB7093":"PaleVioletRed" \
,"#DBDBDB":"gray86" \
,"#DC143C":"crimson" \
,"#DCDCDC":"gainsboro" \
,"#DDA0DD":"plum" \
,"#DEB887":"burlywood" \
,"#DEDEDE":"gray87" \
,"#E066FF":"MediumOrchid1" \
,"#E0E0E0":"gray88" \
,"#E0EEE0":"honeydew2" \
,"#E0EEEE":"azure2" \
,"#E0FFFF":"LightCyan" \
,"#E0FFFF":"LightCyan1" \
,"#E3E3E3":"gray89" \
,"#E5E5E5":"gray90" \
,"#E6E6FA":"lavender" \
,"#E8E8E8":"gray91" \
,"#E9967A":"DarkSalmon" \
,"#EBEBEB":"gray92" \
,"#EDEDED":"gray93" \
,"#EE0000":"red2" \
,"#EE00EE":"magenta2" \
,"#EE1289":"DeepPink2" \
,"#EE2C2C":"firebrick2" \
,"#EE30A7":"maroon2" \
,"#EE3A8C":"VioletRed2" \
,"#EE3B3B":"brown2" \
,"#EE4000":"OrangeRed2" \
,"#EE5C42":"tomato2" \
,"#EE6363":"IndianRed2" \
,"#EE6A50":"coral2" \
,"#EE6AA7":"HotPink2" \
,"#EE7600":"DarkOrange2" \
,"#EE7621":"chocolate2" \
,"#EE7942":"sienna2" \
,"#EE799F":"PaleVioletRed2" \
,"#EE7AE9":"orchid2" \
,"#EE8262":"salmon2" \
,"#EE82EE":"violet" \
,"#EE9572":"LightSalmon2" \
,"#EE9A00":"orange2" \
,"#EE9A49":"tan2" \
,"#EEA2AD":"LightPink2" \
,"#EEA9B8":"pink2" \
,"#EEAD0E":"DarkGoldenrod2" \
,"#EEAEEE":"plum2" \
,"#EEB422":"goldenrod2" \
,"#EEB4B4":"RosyBrown2" \
,"#EEC591":"burlywood2" \
,"#EEC900":"gold2" \
,"#EECBAD":"PeachPuff2" \
,"#EECFA1":"NavajoWhite2" \
,"#EED2EE":"thistle2" \
,"#EED5B7":"bisque2" \
,"#EED5D2":"MistyRose2" \
,"#EED8AE":"wheat2" \
,"#EEDC82":"LightGoldenrod2" \
,"#EEDD82":"LightGoldenrod" \
,"#EEDFCC":"AntiqueWhite2" \
,"#EEE0E5":"LavenderBlush2" \
,"#EEE5DE":"seashell2" \
,"#EEE685":"khaki2" \
,"#EEE8AA":"PaleGoldenrod" \
,"#EEE8CD":"cornsilk2" \
,"#EEE9BF":"LemonChiffon2" \
,"#EEE9E9":"snow2" \
,"#EEEE00":"yellow2" \
,"#EEEED1":"LightYellow2" \
,"#EEEEE0":"ivory2" \
,"#F08080":"LightCoral" \
,"#F0E68C":"khaki" \
,"#F0F0F0":"gray94" \
,"#F0F8FF":"AliceBlue" \
,"#F0FFF0":"honeydew" \
,"#F0FFF0":"honeydew1" \
,"#F0FFFF":"azure" \
,"#F0FFFF":"azure1" \
,"#F2F2F2":"gray95" \
,"#F4A460":"SandyBrown" \
,"#F5DEB3":"wheat" \
,"#F5F5DC":"beige" \
,"#F5F5F5":"WhiteSmoke" \
,"#F5F5F5":"gray96" \
,"#F5FFFA":"MintCream" \
,"#F7F7F7":"gray97" \
,"#F8F8FF":"GhostWhite" \
,"#FA8072":"salmon" \
,"#FAEBD7":"AntiqueWhite" \
,"#FAF0E6":"linen" \
,"#FAFAD2":"LightGoldenrodYellow" \
,"#FAFAFA":"gray98" \
,"#FCFCFC":"gray99" \
,"#FDF5E6":"OldLace" \
,"#FF0000":"red" \
,"#FF0000":"red1" \
,"#FF00FF":"magenta1" \
,"#FF00FF":"fuchsia" \
,"#FF00FF":"magenta" \
,"#FF1493":"DeepPink" \
,"#FF1493":"DeepPink1" \
,"#FF3030":"firebrick1" \
,"#FF34B3":"maroon1" \
,"#FF3E96":"VioletRed1" \
,"#FF4040":"brown1" \
,"#FF4500":"OrangeRed" \
,"#FF4500":"OrangeRed1" \
,"#FF6347":"tomato" \
,"#FF6347":"tomato1" \
,"#FF69B4":"HotPink" \
,"#FF6A6A":"IndianRed1" \
,"#FF6EB4":"HotPink1" \
,"#FF7256":"coral1" \
,"#FF7F00":"DarkOrange1" \
,"#FF7F24":"chocolate1" \
,"#FF7F50":"coral" \
,"#FF8247":"sienna1" \
,"#FF82AB":"PaleVioletRed1" \
,"#FF83FA":"orchid1" \
,"#FF8C00":"DarkOrange" \
,"#FF8C69":"salmon1" \
,"#FFA07A":"LightSalmon" \
,"#FFA07A":"LightSalmon1" \
,"#FFA500":"orange" \
,"#FFA500":"orange1" \
,"#FFA54F":"tan1" \
,"#FFAEB9":"LightPink1" \
,"#FFB5C5":"pink1" \
,"#FFB6C1":"LightPink" \
,"#FFB90F":"DarkGoldenrod1" \
,"#FFBBFF":"plum1" \
,"#FFC0CB":"pink" \
,"#FFC125":"goldenrod1" \
,"#FFC1C1":"RosyBrown1" \
,"#FFD39B":"burlywood1" \
,"#FFD700":"gold" \
,"#FFD700":"gold1" \
,"#FFDAB9":"PeachPuff" \
,"#FFDAB9":"PeachPuff1" \
,"#FFDEAD":"NavajoWhite" \
,"#FFDEAD":"NavajoWhite1" \
,"#FFE1FF":"thistle1" \
,"#FFE4B5":"moccasin" \
,"#FFE4C4":"bisque" \
,"#FFE4C4":"bisque1" \
,"#FFE4E1":"MistyRose" \
,"#FFE4E1":"MistyRose1" \
,"#FFE7BA":"wheat1" \
,"#FFEBCD":"BlanchedAlmond" \
,"#FFEC8B":"LightGoldenrod1" \
,"#FFEFD5":"PapayaWhip" \
,"#FFEFDB":"AntiqueWhite1" \
,"#FFF0F5":"LavenderBlush" \
,"#FFF0F5":"LavenderBlush1" \
,"#FFF5EE":"seashell" \
,"#FFF5EE":"seashell1" \
,"#FFF68F":"khaki1" \
,"#FFF8DC":"cornsilk" \
,"#FFF8DC":"cornsilk1" \
,"#FFFACD":"LemonChiffon" \
,"#FFFACD":"LemonChiffon1" \
,"#FFFAF0":"FloralWhite" \
,"#FFFAFA":"snow" \
,"#FFFAFA":"snow1" \
,"#FFFF00":"yellow" \
,"#FFFF00":"yellow1" \
,"#FFFFE0":"LightYellow" \
,"#FFFFE0":"LightYellow1" \
,"#FFFFF0":"ivory" \
,"#FFFFF0":"ivory1" \
,"#FFFFFF":"white" \
,"#FFFFFF":"gray100" \
}


def raise_invalid_param_error(param, cause):
    """
        Raises invalid param error

        :param param: the param to raise error for
        :param cause: the cause of the error
    """
    raise APIError(code=f'Invalid Input: {param}',
                   cause=cause,
                   message=f'Please try again with a valid {param}',
                   status=status_codes.HTTP_BAD_REQUEST,
                   extended_info=build_uv_svr_error_response(
                       server_message=f'Invalid Input: {param}',
                       server_control_name=f'errInvalid{param.capitalize()}')
                   )


def validate_params(params, required_params=None):
    """
        Validates that a set of params is present and matches the required type.

        :param params: the params to be validated
        :param required_params: the params that must be present
        :return: None
    """
    if required_params:
        for param, param_type in required_params.items():
            if param not in params:
                raise_invalid_param_error(param, f'{param} is required')
            if type(params[param]) is not type(param_type):
                raise_invalid_param_error(param, f'{param} must be type {type(param).__name__}')
    return None


def convert_param_list_values(query_param):
    """
        Converts the query parameters from string to integer numbers.

        :param query_param: list of params to be converted
        :return: query_param_int_list: list of params in int values
    """
    query_param_int_list = []
    try:
        for param in query_param:
            color_code_int_value = int(param)
            query_param_int_list.append(color_code_int_value)
    except ValueError as e:
        raise APIError(code=f'Invalid Input: {query_param} not a number',
                       cause=f'Invalid Input: {e}',
                       message=f'Please enter list of 3 numbers for RGB color code',
                       status=status_codes.HTTP_BAD_REQUEST,
                       extended_info=build_uv_svr_error_response(
                         server_message=f'Invalid Input: {query_param}',
                         server_control_name=f'errInvalidColorCode'))
    return query_param_int_list