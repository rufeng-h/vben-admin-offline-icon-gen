const fs = require('fs');
const {lookupCollection} = require('@iconify/json')
const {getIcons} = require('@iconify/utils')


const icons = {
    'material-symbols': ['arrow-upward', 'arrow-downward'],
    'simple-icons': ['about-dot-me'],
    'fluent-mdl2': ['breakfast'],
    'ri': ['money-cny-box-line'],
    'icon-park-solid':['resting']
}


const getIconSet = async (prefix) => {
    return await lookupCollection(prefix);
}

const run = async (icons) => {
    const iconSetData = [];
    for (let prefix in icons) {
        const iconSet = await getIconSet(prefix);
        const IconsSuffixs = icons[prefix];
        const iconJson = getIcons(iconSet, IconsSuffixs, true);
        if (!!iconJson) {
            iconJson['lastModified'] = undefined;
        }
        // for (let i = 0; i < iconJson.length; i++) {
        //     if (!!iconJson[i]) {
        //         throw new Error("找不到" + prefix + ":" + IconsSuffixs[i])
        //     }
        // }
        iconSetData.push(iconJson);
    }
    const str = JSON.stringify(iconSetData);
    fs.writeFileSync('./icons.json', str, {
        encoding: 'utf-8'
    });
}

run(icons);