// import { setupDevtools } from "../devtools"
import functions from './functions'
import { createScript } from '../utils'

function createProduct (id, name, price, brand, category, index) {
    return {
        item_id: id,
        item_name: name,
        price: price,
        item_brand: brand,
        item_category: category,
        index: index
    }
}

/**
 * Map the fields from incoming products
 * to a different name example: 
 * {price: 15} > unit_price > {unit_price: 15}
 * 
 * @param {Array} products - List of products
 * @param {Object} mapping - Fields to map to a new name
 * @return Products with a new field name
 */
function mapToFields (products, mapping) {
    return products.map((product) => {
        var entries = Object.entries(mapping)
        var newItems = {}

        entries.forEach((entry) => {
            newItems[entry[1]] = product[entry[0]]
        })

        return newItems
    })
}

function createGoogleAnalytics (tag, options) {
    const { currency, brand, optimize_tag, debug } = options

    functions.DEFAULT_CURRENCY = currency || functions.DEFAULT_CURRENCY
    functions.DEFAULT_BRAND = brand

    // 1. Create the no script tag
    const url = new URL('https://www.googletagmanager.com/gtag/js')
    url.searchParams.append('id', tag)
    const noScript = createScript(url.toString(), true)
    document.head.appendChild(noScript)

    let datalayerSettings = null
    if (debug) {
        datalayerSettings = `{ currency: '${functions.DEFAULT_CURRENCY}', debug_mode: true }`
    } else {
        datalayerSettings = `{ currency: '${functions.DEFAULT_CURRENCY}' }`
    }

    // 2. Create the main Analytics script tag
    const script = document.createElement('script')
    const content = document.createTextNode(`
    window.dataLayer = window.dataLayer || []
    function gtag() { dataLayer.push(arguments) }
    gtag('js', 1 * new Date())
    gtag('config', '${tag}', ${datalayerSettings})`)

    script.appendChild(content)

    document.head.appendChild(script)
    script.parentNode.insertBefore(noScript, script)

    if (optimize_tag) {
        // 3. Google Optimize
        const url = new URL('https://www.googleoptimize.com/optimize.js')
        url.searchParams.append('id', optimize_tag)
        const optimize = createScript(url, true)
        document.head.appendChild(optimize)
    }

    return {
        install: (app) => {
            app.config.globalProperties.$analytics = {
                google: functions
            }

            window.VueAnalytics = {
                google: functions
            }
        }
    }
}

export {
    createProduct,
    createGoogleAnalytics,
    mapToFields
}
