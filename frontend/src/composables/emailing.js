/**
 * Helper function to replace variable placeholders
 * in an email (object, body) text
 * 
 */ 
export function useEmailUtilities () {
  /**
   * @param text - text to replace
   * @param queryData - dictionnary to use in order to return the replacement value 
   */
  function replacePlaceholders(text, queryData) {
    if (text.includes('[[') && text.includes(']]')) {
      try {
        return text.replace(/\[\[\s?(\w+)\s?\]\]/g, function (match, placeholder) {
          return queryData[placeholder] || 'Error'
        })
      } catch (e) {
        console.error(e)
        return 'Error'
      }
    } else {
      return text
    }
  }

  return {
    replacePlaceholders
  }
}
