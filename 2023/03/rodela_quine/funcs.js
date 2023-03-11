st = `  #####
      #
  #####
  #
  #####
    #
 #######

#### # #
#    # #
#   ## #
#    # #
#### # #

 ######
      #
 ######
 #
 ######

##### #
    # #
##### ##
#     #
##### #`;

st_hex = '';
st.split('\n').forEach((line) => {
    n = 0;
    k = 1;
    for (let i = 0; i < line.length; i++) {
        if (line[i] == '#') {
            n += k;
        }
        k <<= 1;
    }
    st_hex += n.toString(16).padStart(2, '0');
});

console.log(st_hex);

s = 'testaoskfgawogvk';
s = s.repeat(500);

/**
 * 
 * @param {String} string 
 * @param {String} structure 
 */

a = 8;
b = 4;

function format(string, structure) {
    idx = 0;
    out_s = '';
    structure.match(/.{1,2}/g).forEach((value) => {
        for (let i = 0; i < b; i++) {
            line_structure = parseInt(value, 16);
            tmp = line_structure;
            line = '';
            while (tmp) {
                if (tmp % 2) {
                    line += s.slice(idx, idx + a);
                    idx += a;
                } else {
                    line += ' '.repeat(a);
                }
                tmp >>= 1;
            }
            out_s += line + '\n';
        }
    });
    return out_s;
}

